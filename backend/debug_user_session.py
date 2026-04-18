import sqlite3
import json

def check_user_session():
    db_path = "test_results.db"
    conn = sqlite3.connect(db_path)
    # Set row factory to access columns by name
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    query = "SELECT id, user_name, started_at, finished_at, score, percentage, answers_json FROM test_sessions WHERE user_name LIKE ?"
    
    # Using LIKE to be safe with potential encoding or partial matches
    cursor.execute(query, ('%албул%',))
    rows = cursor.fetchall()

    if not rows:
        print("No sessions found for user 'албул'.")
        return

    print(f"Found {len(rows)} session(s) for user 'албул':\n")
    for row in rows:
        print("-" * 40)
        print(f"ID: {row['id']}")
        print(f"User Name: {row['user_name']}")
        print(f"Started At: {row['started_at']}")
        print(f"Finished At: {row['finished_at']}")
        print(f"Score: {row['score']}")
        print(f"Percentage: {row['percentage']}%")
        
        answers_json = row['answers_json']
        if answers_json:
            try:
                # answers_json might be stored as a string or already parsed depending on how sqlite3/sqlalchemy handled it
                if isinstance(answers_json, str):
                    answers = json.loads(answers_json)
                else:
                    answers = answers_json
                print(f"Answers Stored: Yes ({len(answers)} answers)")
            except Exception as e:
                print(f"Answers Stored: Yes (But failed to parse: {e})")
        else:
            print("Answers Stored: No (None or Empty)")
        print("-" * 40)

    conn.close()

if __name__ == "__main__":
    check_user_session()
