from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from models.questions_data import SCHREIBEN_AUFGABEN
import io, textwrap
from datetime import datetime

router = APIRouter()

class BriefSubmit(BaseModel):
    test_number: int
    user_name: str
    text: str

@router.get("/aufgabe/{test_number}")
def get_aufgabe(test_number: int):
    if test_number not in SCHREIBEN_AUFGABEN:
        raise HTTPException(status_code=404, detail="Test not found")
    return SCHREIBEN_AUFGABEN[test_number]

@router.post("/download-pdf/{test_number}")
def download_brief(test_number: int, data: BriefSubmit):
    """Generate a downloadable PDF of the written letter"""
    if test_number not in SCHREIBEN_AUFGABEN:
        raise HTTPException(status_code=404, detail="Test not found")

    aufgabe = SCHREIBEN_AUFGABEN[test_number]
    text = data.text.strip()
    word_count = len(text.split()) if text else 0

    # Build plain-text content that will be turned into PDF-like text
    content = _build_pdf_content(data.user_name, aufgabe, text, word_count)

    # Stream as plain UTF-8 text (client downloads)
    buf = io.BytesIO(content.encode("utf-8"))
    filename = f"Brief_Test{test_number}_{data.user_name.replace(' ','_')}.txt"
    return StreamingResponse(
        buf,
        media_type="text/plain; charset=utf-8",
        headers={"Content-Disposition": f"attachment; filename=\"{filename}\""}
    )

def _build_pdf_content(user_name, aufgabe, text, word_count):
    sep  = "=" * 62
    sep2 = "-" * 62
    now  = datetime.now().strftime("%d.%m.%Y %H:%M")

    leitpunkte_str = "\n".join(
        f"  {i+1}. {lp}" for i, lp in enumerate(aufgabe["leitpunkte"])
    )
    kriterien_str = "\n".join(
        f"  • {k}" for k in aufgabe["bewertungskriterien"]
    )

    # Check leitpunkte coverage (basic keyword scan)
    lp_status = []
    for i, lp in enumerate(aufgabe["leitpunkte"]):
        key_words = lp.lower().split()[:4]
        found = any(kw in text.lower() for kw in key_words if len(kw) > 4)
        lp_status.append(("✓" if found else "○") + f" Leitpunkt {i+1}: {lp}")

    wc_ok = aufgabe["woerter_min"] <= word_count <= aufgabe["woerter_max"]
    wc_symbol = "✓" if wc_ok else ("↑" if word_count < aufgabe["woerter_min"] else "↓")

    return f"""{sep}
GOETHE-ZERTIFIKAT B1 — SCHRIFTLICHER AUSDRUCK
{sep}
Teilnehmer:  {user_name}
Test:        Test {aufgabe["test"]} — {aufgabe["thema"]}
Datum:       {now}
{sep}

AUFGABE (Teil 4 — Brief schreiben)
{sep2}
{aufgabe["situation"]}

LEITPUNKTE:
{leitpunkte_str}

HINWEIS: {aufgabe["hinweise"]}
{sep2}

IHR BRIEF
{sep2}
{aufgabe["beispiel_anrede"]}

{text if text else "[Kein Text eingegeben]"}

{aufgabe["beispiel_gruss"]}
{sep2}

AUSWERTUNG
{sep2}
Wörteranzahl:   {word_count} Wörter  {wc_symbol}  (Ziel: {aufgabe["woerter_min"]}–{aufgabe["woerter_max"]})

Leitpunkte (automatische Prüfung):
{chr(10).join("  " + s for s in lp_status)}

Bewertungskriterien für den Prüfer:
{kriterien_str}

HINWEIS: Die automatische Leitpunkt-Prüfung ist eine
Orientierungshilfe. Die endgültige Bewertung erfolgt
durch einen zertifizierten Prüfer.
{sep}
Erstellt mit Deutsch B1 Übungstest — Schreibaufgabe
{sep}
"""

