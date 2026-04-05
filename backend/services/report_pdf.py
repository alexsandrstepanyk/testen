import io
import json
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def build_test_report_pdf(session, questions):
    questions_by_id = {q["id"]: q for q in questions}
    answers = parse_answers(session.answers_json)
    mistakes = collect_mistakes(questions_by_id, answers)

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
        lines = wrap_text(text, width_chars)
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

    schreiben_text = extract_schreiben_text(answers)
    if schreiben_text:
        ensure_space(120)
        write_line("Teil 4 - Ihr Brief", size=13, bold=True, gap=18)
        write_wrapped(schreiben_text, size=10, width_chars=100)

    c.showPage()
    c.save()
    pdf_stream.seek(0)
    return pdf_stream.getvalue(), mistakes


def parse_answers(answers_json):
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


def extract_schreiben_text(answers):
    schreiben = answers.get("schreiben")
    if isinstance(schreiben, str):
        return schreiben.strip()
    if isinstance(schreiben, dict):
        return str(schreiben.get("text", "")).strip()
    return ""


def collect_mistakes(questions_by_id, answers):
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


def wrap_text(text, width_chars):
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
