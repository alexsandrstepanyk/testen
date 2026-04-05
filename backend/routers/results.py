from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import desc, func
from models.database import get_db
from models.models import TestSession
from models.questions_data import get_questions_for_test
import io
import json

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

router = APIRouter()

@router.get("/leaderboard")
def get_leaderboard(limit: int = Query(default=50, le=200),
                    test_number: int = Query(default=0),
                    db: Session = Depends(get_db)):
    q = db.query(TestSession).filter(TestSession.score.isnot(None))
    if test_number in range(1, 6):
        q = q.filter(TestSession.test_number == test_number)
    sessions = q.order_by(desc(TestSession.score), TestSession.duration_seconds).limit(limit).all()
    return {"leaderboard": [
        {"rank": i+1, "user_name": s.user_name, "test_number": s.test_number or 1,
         "score": s.score, "total_questions": s.total_questions,
         "percentage": s.percentage, "duration_seconds": s.duration_seconds,
         "passed": s.passed, "teil1_score": s.teil1_score,
         "teil2_score": s.teil2_score, "teil3_score": s.teil3_score,
         "teil4_score": s.teil4_score or 0,
         "finished_at": s.finished_at.isoformat() if s.finished_at else None}
        for i, s in enumerate(sessions)
    ], "total_entries": len(sessions)}

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(TestSession).filter(TestSession.score.isnot(None)).count()
    if not total:
        return {"total_attempts":0,"pass_rate":0,"avg_score":0,"avg_duration_seconds":0}
    passed = db.query(TestSession).filter(TestSession.passed==True).count()
    avg_s = db.query(func.avg(TestSession.score)).filter(TestSession.score.isnot(None)).scalar()
    avg_d = db.query(func.avg(TestSession.duration_seconds)).filter(TestSession.duration_seconds.isnot(None)).scalar()
    return {"total_attempts":total,"total_passed":passed,
            "pass_rate":round(passed/total*100,1),
            "avg_score":round(avg_s,1) if avg_s else 0,
            "avg_duration_seconds":int(avg_d) if avg_d else 0}

@router.delete("/leaderboard/clear")
def clear(db: Session = Depends(get_db)):
    db.query(TestSession).delete(); db.commit()
    return {"message": "All results cleared"}


@router.get("/report/{session_id}/pdf")
def download_result_pdf(
    session_id: int,
    user_name: str = Query(..., min_length=1),
    db: Session = Depends(get_db),
):
    session = db.query(TestSession).filter(TestSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    if session.score is None:
        raise HTTPException(status_code=400, detail="Session is not finished yet")
    if session.user_name.strip().lower() != user_name.strip().lower():
        raise HTTPException(status_code=403, detail="This report is not available for this user")

    questions = get_questions_for_test(session.test_number or 1)
    questions_by_id = {q["id"]: q for q in questions}
    answers = _parse_answers(session.answers_json)
    mistakes = _collect_mistakes(questions_by_id, answers)

    pdf_stream = io.BytesIO()
    c = canvas.Canvas(pdf_stream, pagesize=A4)
    width, height = A4
    y = height - 40

    def ensure_space(min_y=70):
        nonlocal y
        if y < min_y:
            c.showPage()
            y = height - 40

    def write_line(text, size=11, bold=False, indent=0, gap=14):
        nonlocal y
        ensure_space()
        font = "Helvetica-Bold" if bold else "Helvetica"
        c.setFont(font, size)
        c.drawString(40 + indent, y, text)
        y -= gap

    def write_wrapped(text, size=10, indent=0, width_chars=105, gap=12):
        nonlocal y
        lines = _wrap_text(text, width_chars)
        for line in lines:
            ensure_space()
            c.setFont("Helvetica", size)
            c.drawString(40 + indent, y, line)
            y -= gap

    total_points = (session.total_questions or 45) + 10
    finished = session.finished_at.isoformat() if session.finished_at else "-"

    write_line("Deutsch B1 - Testbericht", size=16, bold=True, gap=20)
    write_line(f"Name: {session.user_name}")
    write_line(f"Test: {session.test_number or 1}")
    write_line(f"Session ID: {session.id}")
    write_line(f"Abgeschlossen: {finished}")
    write_line(f"Ergebnis: {session.score}/{total_points} ({session.percentage}%)", bold=True)
    write_line(f"Status: {'Bestanden' if session.passed else 'Nicht bestanden'}")
    write_line(f"Zeit: {session.duration_seconds or 0} Sekunden")
    write_line(
        "Teilpunkte: "
        f"Teil 1 {session.teil1_score or 0}/20 | "
        f"Teil 2 {session.teil2_score or 0}/10 | "
        f"Teil 3 {session.teil3_score or 0}/15 | "
        f"Teil 4 {session.teil4_score or 0}/10"
    )

    y -= 8
    write_line("Fehleranalyse", size=13, bold=True, gap=18)

    if not mistakes:
        write_line("Keine Fehler erkannt. Sehr gute Leistung.", size=11)
    else:
        write_line(f"Anzahl der Fehler: {len(mistakes)}", size=11)
        y -= 4
        for idx, m in enumerate(mistakes, start=1):
            ensure_space(120)
            write_line(f"{idx}. Teil {m['teil']} - Frage {m['question_id']}", bold=True)
            write_wrapped(f"Frage: {m['question_text']}", indent=12)
            if m.get("context"):
                write_wrapped(f"Text: {m['context']}", indent=12)
            write_wrapped(f"Ihre Antwort: {m['user_answer_display']}", indent=12)
            write_wrapped(f"Richtige Antwort: {m['correct_answer_display']}", indent=12)
            if m.get("explanation"):
                write_wrapped(f"Erklaerung: {m['explanation']}", indent=12)
            y -= 6

    schreiben_text = _extract_schreiben_text(answers)
    if schreiben_text:
        ensure_space(120)
        write_line("Teil 4 - Ihr Brief", size=13, bold=True, gap=18)
        write_wrapped(schreiben_text, size=10, width_chars=100)

    c.showPage()
    c.save()
    pdf_stream.seek(0)
    safe_name = session.user_name.replace(" ", "_")
    filename = f"Testbericht_T{session.test_number}_{safe_name}_{session.id}.pdf"
    return StreamingResponse(
        pdf_stream,
        media_type="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


def _parse_answers(answers_json):
    if not answers_json:
        return {}
    if isinstance(answers_json, str):
        try:
            return json.loads(answers_json)
        except Exception:
            return {}
    if isinstance(answers_json, dict):
        return answers_json
    return {}


def _extract_schreiben_text(answers):
    schreiben = answers.get("schreiben")
    if isinstance(schreiben, str):
        return schreiben.strip()
    if isinstance(schreiben, dict):
        return str(schreiben.get("text", "")).strip()
    return ""


def _collect_mistakes(questions_by_id, answers):
    mistakes = []
    answer_map = {"a": 0, "b": 1, "c": 2}

    for key, user_answer in answers.items():
        if key == "schreiben":
            continue
        try:
            qid = int(key)
        except Exception:
            continue
        question = questions_by_id.get(qid)
        if not question:
            continue

        qtype = question.get("type")
        correct = question.get("correct")
        is_correct = False
        user_display = str(user_answer)
        correct_display = str(correct)

        if qtype == "rf":
            u = str(user_answer).lower()
            is_correct = (u == "true" and bool(correct)) or (u == "false" and not bool(correct))
            user_display = "Richtig" if u == "true" else "Falsch"
            correct_display = "Richtig" if bool(correct) else "Falsch"
        else:
            ua_str = str(user_answer).lower()
            if ua_str.isdigit():
                u_idx = int(ua_str)
            else:
                u_idx = answer_map.get(ua_str, -1)
            is_correct = (u_idx == correct)
            options = question.get("options") or []
            if 0 <= u_idx < len(options):
                label = ua_str if not ua_str.isdigit() else ["a", "b", "c"][u_idx] if u_idx < 3 else str(u_idx)
                user_display = f"{label}: {options[u_idx]}"
            if isinstance(correct, int) and 0 <= correct < len(options):
                correct_display = f"{['a','b','c'][correct]}: {options[correct]}"

        if not is_correct:
            mistakes.append({
                "question_id": qid,
                "teil": question.get("teil", 0),
                "question_text": question.get("question", ""),
                "context": question.get("context", ""),
                "explanation": question.get("explanation", ""),
                "user_answer_display": user_display,
                "correct_answer_display": correct_display,
            })

    return sorted(mistakes, key=lambda m: (m["teil"], m["question_id"]))


def _wrap_text(text, width_chars):
    if not text:
        return [""]
    words = str(text).replace("\n", " \n ").split()
    lines = []
    current = ""
    for word in words:
        if word == "\n":
            lines.append(current.rstrip())
            current = ""
            continue
        candidate = (current + " " + word).strip()
        if len(candidate) <= width_chars:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines
