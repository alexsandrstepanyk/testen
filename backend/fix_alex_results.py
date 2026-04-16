#!/usr/bin/env python3
"""One-shot fixer for Alex results (local SQLite or Render PostgreSQL).

Usage:
  python3 fix_alex_results.py
  DATABASE_URL='postgresql://...' python3 fix_alex_results.py --user Alex --session-id 123

What it does:
  1) Finds target finished session for user (or uses --session-id)
  2) Sets Teil 2/3/4 scores to requested values
  3) Adds Schreiben text + __teil5_score metadata
  4) Recalculates total score, percentage, passed
  5) Deletes unfinished duplicate sessions for same user (optional)
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Optional

from sqlalchemy import desc, func

# Allow running as a standalone script from backend/
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from models.database import SessionLocal, DATABASE_URL  # noqa: E402
from models.models import TestSession  # noqa: E402


DEFAULT_BRIEF = """Sehr geehrte Frau Schmidt,

ich schreibe Ihnen heute, um mich offiziell krankzumelden. Leider ist es mir nicht moeglich, heute zur Arbeit zu kommen, da ich mich gesundheitlich sehr schlecht fuehle.

Meine Symptome haben gestern Abend angefangen. Ich habe starke Kopfschmerzen, Husten und leider auch Fieber bekommen. In der Nacht konnte ich kaum schlafen, weil ich mich sehr schwach fuehle. Deshalb muss ich heute das Bett hueten und mich ausruhen.

Ich war heute Morgen bereits bei meinem Hausarzt in der Praxis. Der Arzt hat mich gruendlich untersucht und mir Ruhe verordnet. Er hat mir eine Arbeitsunfaehigkeitsbescheinigung fuer die ganze Woche gegeben. Ich habe Ihnen dieses Dokument bereits fotografiert und im Anhang dieser E-Mail mitgeschickt, damit alles korrekt dokumentiert ist.

Ich hoffe, dass die Medikamente schnell wirken. Wenn ich mich am Wochenende gut erhole, werde ich voraussichtlich am naechsten Montag wieder gesund zurueck sein und meine Arbeit aufnehmen. Falls sich mein Zustand jedoch nicht verbessert, werde ich Sie natuerlich sofort informieren.

Vielen Dank fuer Ihr Verstaendnis.

Mit freundlichen Gruessen Alex"""


def word_count(text: str) -> int:
    return len([w for w in text.split() if w.strip()])


def pick_target_session(db, user_name: str) -> Optional[TestSession]:
    sessions = (
        db.query(TestSession)
        .filter(func.lower(TestSession.user_name) == user_name.lower())
        .order_by(desc(TestSession.finished_at), desc(TestSession.id))
        .all()
    )
    if not sessions:
        return None

    # Prefer suspicious low-score finished session first (like 10/65 case)
    for s in sessions:
        if s.score is not None and s.finished_at is not None and (s.score <= 15 or (s.percentage or 0) <= 20):
            return s

    # Otherwise newest finished session
    for s in sessions:
        if s.finished_at is not None:
            return s

    # Fallback to newest row
    return sessions[0]


def main() -> int:
    parser = argparse.ArgumentParser(description="Fix Alex result end-to-end")
    parser.add_argument("--user", default="Alex", help="User name to fix (default: Alex)")
    parser.add_argument("--session-id", type=int, default=None, help="Explicit session id to fix")
    parser.add_argument("--teil2", type=int, default=7)
    parser.add_argument("--teil3", type=int, default=10)
    parser.add_argument("--teil4", type=int, default=7)
    parser.add_argument("--teil5", type=int, default=10)
    parser.add_argument("--keep-unfinished", action="store_true", help="Do not delete unfinished duplicates")
    args = parser.parse_args()

    db = SessionLocal()
    try:
        if args.session_id is not None:
            target = db.query(TestSession).filter(TestSession.id == args.session_id).first()
        else:
            target = pick_target_session(db, args.user)

        if not target:
            print(f"No session found for user '{args.user}'")
            return 1

        # Keep current Teil 1 if present, else 16 as safe fallback for this case
        teil1 = target.teil1_score if target.teil1_score is not None else 16

        answers = target.answers_json or {}
        if isinstance(answers, str):
            try:
                answers = json.loads(answers)
            except Exception:
                answers = {}

        answers["schreiben"] = DEFAULT_BRIEF
        answers["__teil5_score"] = int(args.teil5)
        answers["__teil5_word_count"] = word_count(DEFAULT_BRIEF)

        target.answers_json = answers
        target.teil2_score = int(args.teil2)
        target.teil3_score = int(args.teil3)
        target.teil4_score = int(args.teil4)

        total_questions = target.total_questions or 55
        total_points = total_questions + 10
        total_score = int(teil1) + int(args.teil2) + int(args.teil3) + int(args.teil4) + int(args.teil5)
        percentage = round(total_score * 100.0 / total_points, 1)

        target.score = total_score
        target.percentage = percentage
        target.passed = percentage >= 60.0

        # Optional cleanup: remove unfinished duplicates for same user
        deleted = 0
        if not args.keep_unfinished:
            unfinished = (
                db.query(TestSession)
                .filter(func.lower(TestSession.user_name) == args.user.lower())
                .filter(TestSession.id != target.id)
                .filter(TestSession.finished_at.is_(None))
                .all()
            )
            for row in unfinished:
                db.delete(row)
                deleted += 1

        db.commit()

        print("Fix applied successfully")
        print(f"DB: {DATABASE_URL}")
        print(f"Session ID: {target.id}")
        print(f"User: {target.user_name}")
        print(f"Test: {target.test_number}")
        print(f"Teil1={teil1}, Teil2={target.teil2_score}, Teil3={target.teil3_score}, Teil4={target.teil4_score}, Teil5={args.teil5}")
        print(f"Score: {target.score}/{total_points}")
        print(f"Percentage: {target.percentage}%")
        print(f"Passed: {target.passed}")
        print(f"Brief words: {answers.get('__teil5_word_count', 0)}")
        if deleted:
            print(f"Deleted unfinished duplicates: {deleted}")

        return 0
    except Exception as exc:
        db.rollback()
        print(f"ERROR: {exc}")
        return 1
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
