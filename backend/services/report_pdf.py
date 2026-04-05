import io
import json
from reportlab.lib import colors
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

    def write_line(text, size=11, bold=False, indent=0, gap=14, color=colors.black):
        nonlocal y
        ensure_space()
        font = "Helvetica-Bold" if bold else "Helvetica"
        c.setFont(font, size)
        c.setFillColor(color)
        c.drawString(40 + indent, y, text)
        c.setFillColor(colors.black)
        y -= gap

    def write_wrapped(text, size=10, indent=0, width_chars=105, gap=12, color=colors.black):
        nonlocal y
        lines = wrap_text(text, width_chars)
        for line in lines:
            ensure_space()
            c.setFont("Helvetica", size)
            c.setFillColor(color)
            c.drawString(40 + indent, y, line)
            c.setFillColor(colors.black)
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
            write_line(f"{idx}. Teil {m['teil']} - Frage {m['question_id']}", bold=True, color=colors.red)
            write_wrapped(f"Frage: {m['question_text']}", indent=12)
            if m.get("context"):
                write_wrapped(f"Text: {m['context']}", indent=12)
            write_wrapped(f"Ihre Antwort: {m['user_answer_display']}", indent=12, color=colors.red)
            write_wrapped(f"Richtige Antwort: {m['correct_answer_display']}", indent=12)
            if m.get("explanation"):
                write_wrapped(f"Erklaerung: {m['explanation']}", indent=12)
            y -= 6

    ensure_space(140)
    y -= 4
    write_line("Antworten und Loesungen (alle Fragen)", size=13, bold=True, gap=18)
    all_items = collect_all_answer_items(questions, answers)
    for item in all_items:
        ensure_space(90)
        highlight = colors.red if not item["is_correct"] else colors.black
        status = "FALSCH" if not item["is_correct"] else "OK"
        write_line(
            f"Frage {item['question_id']} (Teil {item['teil']}) - {status}",
            bold=True,
            color=highlight,
        )
        write_wrapped(f"Frage: {item['question_text']}", indent=12)
        write_wrapped(f"Ihre Antwort: {item['user_answer_display']}", indent=12, color=highlight)
        write_wrapped(f"Richtige Antwort: {item['correct_answer_display']}", indent=12)
        if item.get("context"):
            write_wrapped(f"Text: {item['context']}", indent=12)
        y -= 3

    schreiben_text = extract_schreiben_text(answers)
    ensure_space(120)
    y -= 4
    write_line("Teil 4 - Ihr Brief", bold=True, gap=16)
    if schreiben_text:
        write_wrapped(schreiben_text, size=10, width_chars=100)
    else:
        write_line("Kein Brieftext gespeichert.", size=10)

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

        is_correct, user_display, correct_display = evaluate_answer(question, user_answer)

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


def evaluate_answer(question, user_answer):
    answer_map = {"a": 0, "b": 1, "c": 2}
    qtype = question.get("type")
    correct = question.get("correct")
    user_display = str(user_answer)
    correct_display = str(correct)
    is_correct = False

    if user_answer is None:
        if qtype == "rf":
            correct_display = "Richtig" if bool(correct) else "Falsch"
        else:
            options = question.get("options") or []
            if isinstance(correct, int) and 0 <= correct < len(options):
                correct_display = f"{['a','b','c'][correct]}: {options[correct]}"
        return False, "Keine Antwort", correct_display

    if qtype == "rf":
        u = str(user_answer).lower()
        is_correct = (u == "true" and bool(correct)) or (u == "false" and not bool(correct))
        user_display = "Richtig" if u == "true" else "Falsch"
        correct_display = "Richtig" if bool(correct) else "Falsch"
        return is_correct, user_display, correct_display

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
    return is_correct, user_display, correct_display


def collect_all_answer_items(questions, answers):
    items = []
    for q in sorted(questions, key=lambda x: (x.get("teil", 0), x.get("id", 0))):
        qid = q.get("id")
        user_answer = answers.get(str(qid), answers.get(qid))
        is_correct, user_display, correct_display = evaluate_answer(q, user_answer)
        items.append({
            "question_id": qid,
            "teil": q.get("teil", 0),
            "question_text": q.get("question", ""),
            "context": q.get("context", ""),
            "is_correct": is_correct,
            "user_answer_display": user_display,
            "correct_answer_display": correct_display,
        })
    return items
