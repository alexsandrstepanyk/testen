import io
import json
from datetime import datetime
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

    def write_wrapped(text, size=10, indent=0, width_chars=105, gap=12, color=colors.black, bold=False):
        nonlocal y
        lines = wrap_text(text, width_chars)
        font = "Helvetica-Bold" if bold else "Helvetica"
        for line in lines:
            ensure_space()
            c.setFont(font, size)
            c.setFillColor(color)
            c.drawString(40 + indent, y, line)
            c.setFillColor(colors.black)
            y -= gap

    answers_meta_score = answers.get("__teil5_score") if isinstance(answers, dict) else None
    teil5_score = int(answers_meta_score) if str(answers_meta_score).isdigit() else max(0, (session.score or 0) - sum([
        session.teil1_score or 0,
        session.teil2_score or 0,
        session.teil3_score or 0,
        session.teil4_score or 0,
    ]))
    total_points = (session.total_questions or 55) + 10
    finished = session.finished_at.isoformat() if session.finished_at else "-"
    percentage = float(session.percentage or 0)
    level = determine_level(percentage)
    solved_tasks = count_solved_tasks(answers)

    # Page 1: certificate page
    accent = colors.HexColor("#0F766E")
    light = colors.HexColor("#E6FFFA")
    dark = colors.HexColor("#0B3B39")

    def center_text(text, y_pos, size=12, bold=False, color=colors.black):
        font = "Helvetica-Bold" if bold else "Helvetica"
        c.setFont(font, size)
        c.setFillColor(color)
        text_width = c.stringWidth(text, font, size)
        c.drawString((width - text_width) / 2, y_pos, text)
        c.setFillColor(colors.black)

    # Double frame
    c.setStrokeColor(accent)
    c.setLineWidth(2)
    c.rect(28, 28, width - 56, height - 56)
    c.setLineWidth(0.8)
    c.rect(40, 40, width - 80, height - 80)

    # Header band
    c.setFillColor(light)
    c.rect(42, height - 150, width - 84, 94, stroke=0, fill=1)
    c.setFillColor(colors.black)

    center_text("URKUNDE", height - 95, size=24, bold=True, color=dark)
    center_text("Deutsch-Prüfung - Stepaniuk", height - 120, size=13, bold=True, color=accent)

    center_text("Hiermit wird bestätigt, dass", height - 195, size=13, color=dark)
    center_text(session.user_name, height - 235, size=30, bold=True, color=colors.HexColor("#111827"))
    c.setStrokeColor(accent)
    c.setLineWidth(1)
    c.line(120, height - 242, width - 120, height - 242)

    center_text("die Sprachprüfung erfolgreich abgeschlossen hat", height - 278, size=12)

    # Level badge
    badge_w, badge_h = 180, 42
    badge_x = (width - badge_w) / 2
    badge_y = height - 338
    c.setFillColor(accent)
    c.roundRect(badge_x, badge_y, badge_w, badge_h, 10, stroke=0, fill=1)
    center_text(f"NIVEAU {level}", badge_y + 14, size=17, bold=True, color=colors.white)

    # Review Pending Badge (if Teil 5 is not manually graded yet)
    is_provisional = True # Future: check if all parts are graded
    if is_provisional:
        p_badge_w, p_badge_h = 100, 20
        c.setFillColor(colors.orange)
        c.roundRect(width - 150, height - 80, p_badge_w, p_badge_h, 4, stroke=0, fill=1)
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(colors.white)
        c.drawCentredString(width - 100, height - 73, "VORLÄUFIG")

    # Stats cards
    card_y = height - 430
    card_w = (width - 140) / 3
    labels = [
        ("Punktzahl", f"{session.score}/{total_points}"),
        ("Ergebnis", f"{session.percentage}%"),
        ("Hören", f"{session.hoeren_score if session.hoeren_score is not None else '–'}/20"),
    ]
    for i, (label, value) in enumerate(labels):
        x = 50 + i * (card_w + 20)
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.roundRect(x, card_y, card_w, 76, 8, stroke=0, fill=1)
        c.setStrokeColor(colors.HexColor("#CBD5E1"))
        c.setLineWidth(0.8)
        c.roundRect(x, card_y, card_w, 76, 8, stroke=1, fill=0)
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#475569"))
        c.drawString(x + 12, card_y + 54, label)
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(colors.HexColor("#0F172A"))
        c.drawString(x + 12, card_y + 30, value)

    # Split Certification Note
    note_y = card_y - 45
    c.setFont("Helvetica-Oblique", 10)
    c.setFillColor(colors.HexColor("#64748B"))
    note_text = "Hinweis: Dieses Zertifikat bestätigt die Ergebnisse der Teile 1–6 (automatisch bewertet)."
    note_text2 = "Teil 7 (Selbstvorstellung) und Teil 8 (Bildbeschreibung) werden vom Lehrer bewertet."
    center_text(note_text, note_y, size=10)
    center_text(note_text2, note_y - 14, size=10)

    # Footer details
    center_text(f"Sitzungs-ID: {session.id}", 170, size=11, color=dark)
    center_text(f"Abgeschlossen: {finished}", 152, size=11, color=dark)

    c.setStrokeColor(colors.HexColor("#334155"))
    c.setLineWidth(0.9)
    c.line(95, 108, 255, 108)
    c.line(width - 255, 108, width - 95, 108)
    c.setFont("Helvetica", 9)
    c.setFillColor(colors.HexColor("#475569"))
    c.drawString(140, 94, "Autorisiert durch Stepaniuk")
    c.drawString(width - 226, 94, "Sprachprüfungsplattform")
    c.setFillColor(colors.black)

    # Page 2: detailed report with all answers and letter
    c.showPage()
    y = height - 40

    write_line("Deutsch - Detaillierter Testbericht", size=16, bold=True, gap=20)
    write_line(f"Name: {session.user_name}")
    write_line(f"Test: {session.test_number or 1}")
    write_line(f"Session ID: {session.id}")
    write_line(f"Abgeschlossen: {finished}")
    write_line(f"Ergebnis: {session.score}/{total_points} ({session.percentage}%)", bold=True)
    write_line(f"Status: {'Bestanden' if session.passed else 'Nicht bestanden'}")
    write_line(f"Zeit: {session.duration_seconds or 0} Sekunden")
    write_line(
        "Teilpunkte: "
        f"Teil 1 (Hören) {session.hoeren_score if session.hoeren_score is not None else '–'}/20 | "
        f"Teil 2 {session.teil1_score or 0}/20 | "
        f"Teil 3 {session.teil2_score or 0}/10 | "
        f"Teil 4 {session.teil3_score or 0}/15 | "
        f"Teil 5 {session.teil4_score or 0}/10 | "
        f"Teil 6 (Schreiben) {teil5_score}/10"
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
    y -= 10
    write_line("Teil 5 - Ihr Brief (Status: Pending Review)", bold=True, color=accent, gap=16)
    if schreiben_text:
        write_wrapped(schreiben_text, size=10, width_chars=100)
    else:
        write_line("Kein Brieftext gespeichert.", size=10)

    # Promotion for Test 6 & 7
    y -= 30
    ensure_space(150)
    c.setStrokeColor(accent)
    c.setLineWidth(1)
    c.setFillColor(light)
    c.roundRect(40, y - 80, width - 80, 100, 10, stroke=1, fill=1)
    
    y -= 25
    write_line("NÄCHSTER SCHRITT: SPLIT CERTIFICATION", size=14, bold=True, indent=20, color=dark)
    write_wrapped("Sie haben die ersten 4 Teile abgeschlossen (automatisch ausgewertet). Teil 5 (Schreiben) wird nun von einem Tutor geprüft.", size=11, indent=20, width_chars=80)
    write_wrapped("Bestehen Sie auch die Aufgaben 6 & 7 (Sprechen), чтобы завершити повний цикл оцінювання", size=11, indent=20, width_chars=80)
    write_wrapped("та отримати фінальний диплом про рівень володіння мовою B1.", size=11, indent=20, width_chars=80, bold=True, color=accent)

    c.save()
    pdf_stream.seek(0)
    return pdf_stream.getvalue(), mistakes


def build_speaking_report_pdf(session):
    """
    Generates a specialized certificate for Speaking tasks (Teil 6 & 7).
    """
    pdf_stream = io.BytesIO()
    try:
        c = canvas.Canvas(pdf_stream, pagesize=A4)
        width, height = A4

        user_name = session.user_name if session.user_name else "Unbekannter Teilnehmer"
        session_id = session.id if session.id else "0"

        accent = colors.HexColor("#7C3AED") # Purple for Speaking
        light = colors.HexColor("#F5F3FF")
        dark = colors.HexColor("#4C1D95")

        def center_text(text, y_pos, size=12, bold=False, color=colors.black):
            font = "Helvetica-Bold" if bold else "Helvetica"
            c.setFont(font, size)
            c.setFillColor(color)
            text_width = c.stringWidth(text, font, size)
            c.drawString((width - text_width) / 2, y_pos, text)
            c.setFillColor(colors.black)

        # Double frame
        c.setStrokeColor(accent)
        c.setLineWidth(2)
        c.rect(28, 28, width - 56, height - 56)
        c.setLineWidth(0.8)
        c.rect(40, 40, width - 80, height - 80)

        # Header
        c.setFillColor(light)
        c.rect(42, height - 150, width - 84, 94, stroke=0, fill=1)
        center_text("SPEAKING & COMMUNICATION", height - 95, size=24, bold=True, color=dark)
        center_text("B1 Deutsch Kompetenzzertifikat", height - 120, size=13, bold=True, color=accent)

        center_text("This certifies that", height - 195, size=13, color=dark)
        center_text(user_name, height - 235, size=30, bold=True, color=colors.HexColor("#111827"))
        
        c.setStrokeColor(accent)
        c.setLineWidth(1)
        c.line(120, height - 242, width - 120, height - 242)

        center_text("has demonstrated proficiency in oral communication", height - 278, size=12)

        # Skills Assessment
        y = height - 340
        center_text("ASSESSED SKILLS", y, size=14, bold=True, color=dark)
        y -= 30

        skills = [
            ("Selbstvorstellung (Self-Intro)", "Fluent and structured personal presentation"),
            ("Bildbeschreibung (Image Description)", "Detailed description and personal opinion"),
            ("Interaction & Vocabulary", "Rich vocabulary and complex sentence structures"),
            ("Pronunciation & Fluency", "Clear articulation and natural speech tempo")
        ]

        for label, desc in skills:
            c.setFont("Helvetica-Bold", 11)
            c.setFillColor(dark)
            c.drawString(80, y, f"• {label}:")
            c.setFont("Helvetica", 11)
            c.setFillColor(colors.black)
            c.drawString(80 + c.stringWidth(f"• {label}: ", "Helvetica-Bold", 11), y, desc)
            y -= 25

        # Badge
        badge_y = 150
        c.setFillColor(accent)
        c.roundRect((width - 200)/2, badge_y, 200, 45, 10, stroke=0, fill=1)
        center_text("COMMUNICATION LEVEL: B1", badge_y + 15, size=14, bold=True, color=colors.white)

        # Footer
        center_text(f"Session ID: {session_id}", 100, size=9, color=colors.HexColor("#6B7280"))
        
        finished_date = datetime.now()
        if hasattr(session, 'finished_at') and session.finished_at:
            finished_date = session.finished_at
        center_text(f"Verified on: {finished_date.strftime('%d.%m.%Y')}", 85, size=9, color=colors.HexColor("#6B7280"))

        c.save()
        pdf_stream.seek(0)
        return pdf_stream.getvalue()
    except Exception as e:
        # If PDF generation fails, we should handle it gracefully or re-raise with context
        print(f"CRITICAL: PDF Generation failed for session {session.id if session else 'unknown'}: {e}")
        raise e


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
        if key == "schreiben" or str(key).startswith("__"):
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
        # Handle both boolean and string representations
        if isinstance(user_answer, bool):
            u_bool = user_answer
        else:
            u = str(user_answer).lower()
            u_bool = u == "true"
        
        is_correct = (u_bool and bool(correct)) or (not u_bool and not bool(correct))
        user_display = "Richtig" if u_bool else "Falsch"
        correct_display = "Richtig" if bool(correct) else "Falsch"
        return is_correct, user_display, correct_display

    # Handle MC/text answers
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


def determine_level(percentage):
    if percentage >= 70:
        return "B1"
    if percentage >= 55:
        return "A2"
    return "A1"


def count_solved_tasks(answers):
    solved = 0
    for key, value in answers.items():
        if key == "schreiben" or str(key).startswith("__"):
            continue
        if value is None:
            continue
        if str(value).strip() == "":
            continue
        solved += 1
    return solved


def build_final_certificate_pdf(session, questions) -> bytes:
    """
    Full final certificate with all 8 parts.
    Max = 105 points.
    """
    answers = parse_answers(session.answers_json)
    teil5_score_val = 0
    if isinstance(answers, dict):
        meta = answers.get("__teil5_score")
        if isinstance(meta, int):
            teil5_score_val = meta
        elif str(meta).isdigit():
            teil5_score_val = int(meta)
        else:
            teil5_score_val = max(0, (session.score or 0) - sum([
                session.teil1_score or 0, session.teil2_score or 0,
                session.teil3_score or 0, session.teil4_score or 0,
            ]))
    schreiben_text = extract_schreiben_text(answers)

    t1 = session.hoeren_score if session.hoeren_score is not None else 0
    t2 = session.teil1_score or 0
    t3 = session.teil2_score or 0
    t4 = session.teil3_score or 0
    t5 = session.teil4_score or 0
    t6 = teil5_score_val
    t7 = session.self_intro_score or 0
    t8 = session.image_description_score or 0

    total_score = t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8
    max_score   = 105
    percentage  = round(total_score / max_score * 100, 1)
    level       = determine_level(percentage)
    finished    = session.finished_at.isoformat() if session.finished_at else "-"

    accent = colors.HexColor("#0F766E")
    light  = colors.HexColor("#E6FFFA")
    dark   = colors.HexColor("#0B3B39")

    pdf_stream = io.BytesIO()
    c = canvas.Canvas(pdf_stream, pagesize=A4)
    width, height = A4

    def center_text(text, y_pos, size=12, bold=False, color=colors.black):
        font = "Helvetica-Bold" if bold else "Helvetica"
        c.setFont(font, size)
        c.setFillColor(color)
        tw = c.stringWidth(text, font, size)
        c.drawString((width - tw) / 2, y_pos, text)
        c.setFillColor(colors.black)

    # ── Page 1: Certificate ──────────────────────────────────────────────────
    c.setStrokeColor(accent); c.setLineWidth(2)
    c.rect(28, 28, width - 56, height - 56)
    c.setLineWidth(0.8)
    c.rect(40, 40, width - 80, height - 80)

    c.setFillColor(light)
    c.rect(42, height - 150, width - 84, 94, stroke=0, fill=1)
    center_text("ABSCHLUSSZERTIFIKAT", height - 95, size=22, bold=True, color=dark)
    center_text("Deutsch-Pruefung B1 - Stepaniuk Sprachplattform", height - 120, size=11, bold=True, color=accent)

    center_text("Hiermit wird bestaetigt, dass", height - 195, size=13, color=dark)
    center_text(session.user_name, height - 235, size=28, bold=True, color=colors.HexColor("#111827"))
    c.setStrokeColor(accent); c.setLineWidth(1)
    c.line(120, height - 242, width - 120, height - 242)
    center_text("alle Pruefungsteile erfolgreich abgeschlossen hat", height - 270, size=12)

    bw, bh = 180, 42
    bx = (width - bw) / 2
    by = height - 328
    c.setFillColor(accent)
    c.roundRect(bx, by, bw, bh, 10, stroke=0, fill=1)
    center_text(f"NIVEAU {level}", by + 14, size=17, bold=True, color=colors.white)

    card_y = height - 430
    card_w = (width - 160) / 4
    card_data = [
        ("Gesamtpunkte", f"{total_score}/{max_score}"),
        ("Ergebnis",     f"{percentage}%"),
        ("Niveau",       level),
        ("Hoeren",       f"{t1}/20"),
    ]
    for i, (label, value) in enumerate(card_data):
        x = 50 + i * (card_w + 20)
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.roundRect(x, card_y, card_w, 70, 8, stroke=0, fill=1)
        c.setStrokeColor(colors.HexColor("#CBD5E1")); c.setLineWidth(0.8)
        c.roundRect(x, card_y, card_w, 70, 8, stroke=1, fill=0)
        c.setFont("Helvetica", 9); c.setFillColor(colors.HexColor("#475569"))
        c.drawString(x + 10, card_y + 50, label)
        c.setFont("Helvetica-Bold", 13); c.setFillColor(colors.HexColor("#0F172A"))
        c.drawString(x + 10, card_y + 28, value)

    tbl_y = card_y - 30
    parts = [
        ("Teil 1 - Hoerverstehen",       t1,  20),
        ("Teil 2 - Multiple Choice",      t2,  20),
        ("Teil 3 - Richtig / Falsch",     t3,  10),
        ("Teil 4 - Leseverstehen",        t4,  15),
        ("Teil 5 - Anzeigen",             t5,  10),
        ("Teil 6 - Schreiben",            t6,  10),
        ("Teil 7 - Selbstvorstellung",    t7,  10),
        ("Teil 8 - Bildbeschreibung",     t8,  10),
    ]
    col_lbl = 50; col_pts = 330; col_bar = 370

    c.setFont("Helvetica-Bold", 10); c.setFillColor(dark)
    c.drawString(col_lbl, tbl_y, "Pruefungsteil")
    c.drawString(col_pts, tbl_y, "Punkte")
    c.drawString(col_bar, tbl_y, "Anteil")
    tbl_y -= 6
    c.setStrokeColor(colors.HexColor("#CBD5E1")); c.setLineWidth(0.5)
    c.line(48, tbl_y, width - 48, tbl_y)
    tbl_y -= 14

    bar_max_w = 130
    for label, pts, mx in parts:
        bar_fill = int(bar_max_w * pts / mx) if mx else 0
        pct = round(pts / mx * 100) if mx else 0
        c.setFillColor(colors.HexColor("#F1F5F9"))
        c.roundRect(col_bar, tbl_y - 2, bar_max_w, 13, 3, stroke=0, fill=1)
        color_bar = accent if pct >= 70 else (colors.HexColor("#F59E0B") if pct >= 50 else colors.HexColor("#EF4444"))
        c.setFillColor(color_bar)
        c.roundRect(col_bar, tbl_y - 2, max(bar_fill, 4), 13, 3, stroke=0, fill=1)
        c.setFont("Helvetica", 10); c.setFillColor(colors.HexColor("#1E293B"))
        c.drawString(col_lbl, tbl_y, label)
        c.setFont("Helvetica-Bold", 10)
        c.drawString(col_pts, tbl_y, f"{pts}/{mx}")
        c.setFont("Helvetica", 9); c.setFillColor(colors.HexColor("#475569"))
        c.drawString(col_bar + bar_max_w + 5, tbl_y, f"{pct}%")
        tbl_y -= 20

    combined_feedback = "\n".join(part for part in [
        session.self_intro_feedback_text or "",
        session.image_description_feedback_text or "",
        session.feedback_text or "",
    ] if part.strip())
    if combined_feedback and tbl_y > 140:
        tbl_y -= 6
        c.setFont("Helvetica-Bold", 10); c.setFillColor(dark)
        c.drawString(50, tbl_y, "Kommentar der Lehrkraft:")
        tbl_y -= 14
        c.setFont("Helvetica-Oblique", 9); c.setFillColor(colors.HexColor("#475569"))
        for line in combined_feedback.split("\n")[:5]:
            if tbl_y < 120:
                break
            c.drawString(60, tbl_y, line[:100])
            tbl_y -= 13

    center_text(f"Sitzungs-ID: {session.id}", 170, size=10, color=dark)
    center_text(f"Abgeschlossen: {finished}", 155, size=10, color=dark)
    c.setStrokeColor(colors.HexColor("#334155")); c.setLineWidth(0.9)
    c.line(95, 112, 255, 112); c.line(width - 255, 112, width - 95, 112)
    c.setFont("Helvetica", 9); c.setFillColor(colors.HexColor("#475569"))
    c.drawString(140, 98, "Autorisiert durch Stepaniuk")
    c.drawString(width - 226, 98, "Sprachpruefungsplattform")

    if schreiben_text:
        c.showPage()
        y2 = height - 40
        c.setFont("Helvetica-Bold", 14); c.setFillColor(dark)
        c.drawString(40, y2, "Teil 6 - Schreiben: Ihr Brieftext"); y2 -= 20
        c.setStrokeColor(accent); c.setLineWidth(0.8)
        c.line(40, y2, width - 40, y2); y2 -= 16
        c.setFont("Helvetica", 10); c.setFillColor(colors.black)
        for line in wrap_text(schreiben_text, 100):
            if y2 < 50:
                c.showPage(); y2 = height - 40
            c.drawString(40, y2, line); y2 -= 13

    c.save()
    pdf_stream.seek(0)
    return pdf_stream.getvalue()
