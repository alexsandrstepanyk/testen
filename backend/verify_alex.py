#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/os/Downloads/deutsch-b1-app 3/backend')

import sqlite3
import json
from models.questions_data import get_questions_for_test

conn = sqlite3.connect("/Users/os/Downloads/deutsch-b1-app 3/backend/test_results.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

# Get Alex's session (ID = 2)
cursor.execute("SELECT * FROM test_sessions WHERE id = 2")
session = cursor.fetchone()

if not session:
    print("No session found")
    exit()

print(f"Checking session for {session['user_name']} (Test {session['test_number']})")
print(f"Current score: {session['score']}/65\n")

# Get answers
answers_json = session['answers_json']
answers = json.loads(answers_json) if answers_json else {}

# Get correct answers
questions = get_questions_for_test(session['test_number'])

print(f"Total questions: {len(questions)}")
print("=" * 80)

# Score each part
scores = {1: 0, 2: 0, 3: 0, 4: 0}
details = {1: [], 2: [], 3: [], 4: []}

for q in sorted(questions, key=lambda x: x['id']):
    qid = q['id']
    qid_str = str(qid)
    user_answer = answers.get(qid_str) if qid_str in answers else answers.get(qid)
    correct = q.get('correct')
    teil = q.get('teil', 1)
    
    if teil not in scores:
        continue
    
    # Determine if correct
    is_correct = False
    
    if q['type'] == 'rf':
        if user_answer is None:
            is_correct = False
        else:
            u = str(user_answer).lower()
            is_correct = (u == "true" and bool(correct)) or (u == "false" and not bool(correct))
    else:  # MC
        if user_answer is None:
            is_correct = False
        else:
            try:
                u_idx = int(user_answer) if isinstance(user_answer, int) else int(str(user_answer))
                is_correct = u_idx == correct
            except:
                is_correct = False
    
    if is_correct:
        scores[teil] += 1
    
    # Store for detailed report
    status = "✓" if is_correct else "✗"
    details[teil].append({
        'id': qid,
        'correct': is_correct,
        'user_answer': user_answer,
        'correct_answer': correct,
        'type': q['type']
    })

# Print scores
print("\nSCORES BY TEIL:")
print(f"Teil 1 (MC):     {scores[1]}/20")
print(f"Teil 2 (RF):     {scores[2]}/10")
print(f"Teil 3 (Text):   {scores[3]}/15")
print(f"Teil 4 (Anzeige):{scores[4]}/10")
print(f"{'─' * 40}")
total = sum(scores.values())
print(f"TOTAL (Teile 1-4): {total}/55")

# Check for Teil 5 in answers
teil5 = 0
if '__teil5_score' in answers:
    try:
        teil5 = int(answers['__teil5_score'])
    except:
        teil5 = 0

print(f"Teil 5 (Writing):  {teil5}/10")
print(f"{'─' * 40}")
final = total + teil5
print(f"FINAL SCORE: {final}/65")
print(f"PERCENTAGE: {round(final/65*100)}%")
print()

# Show incorrect answers
print("=" * 80)
print("\nINCORRECT ANSWERS:")
for teil in [1, 2, 3, 4]:
    incorrect = [d for d in details[teil] if not d['correct']]
    if incorrect:
        print(f"\nTeil {teil} ({len(incorrect)} errors):")
        for d in incorrect[:5]:  # Show first 5
            print(f"  Q{d['id']}: User={d['user_answer']}, Correct={d['correct_answer']}")

conn.close()
