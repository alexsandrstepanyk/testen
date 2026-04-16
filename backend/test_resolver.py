#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/os/Downloads/deutsch-b1-app 3/backend')

from models.questions_data import get_questions_for_test
from services.question_resolver import get_questions_by_test_number

# Test getting questions for test 3
questions = get_questions_for_test(3)
print(f"Questions for test 3 (direct): {len(questions)}")
if questions:
    print(f"First question ID: {questions[0]['id']}")
    print(f"Keys in first question: {list(questions[0].keys())}")
