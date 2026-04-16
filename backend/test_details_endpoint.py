#!/usr/bin/env python3
import urllib.request
import json
import base64
import time

def test_details_endpoint():
    print("=== Testing Alex's Session Details ===\n")
    
    # Test 1: Get sessions list
    print("Test 1: Fetching sessions list...")
    try:
        req = urllib.request.Request('https://deutsch-b1-app.onrender.com/api/teacher/students')
        req.add_header('Authorization', 'Basic ' + base64.b64encode(b'admin:admin').decode())
        resp = urllib.request.urlopen(req, timeout=20)
        data = json.loads(resp.read())
        sessions = data.get('sessions', [])
        alex_sessions = [s for s in sessions if s.get('user_name') == 'Alex']
        
        if alex_sessions:
            print(f"✅ Found {len(alex_sessions)} session(s) for Alex")
            for s in alex_sessions:
                print(f"   - ID: {s['id']}, Test: {s['test_number']}, Score: {s.get('score')}")
        else:
            print("⚠️  No sessions found for Alex")
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # Test 2: Get session details for session 55
    print("\nTest 2: Loading detailed session info for session ID 55...")
    time.sleep(1)  # Small delay
    
    try:
        req = urllib.request.Request('https://deutsch-b1-app.onrender.com/api/teacher/sessions/55/details')
        req.add_header('Authorization', 'Basic ' + base64.b64encode(b'admin:admin').decode())
        resp = urllib.request.urlopen(req, timeout=20)
        data = json.loads(resp.read())
        
        print("✅ SUCCESS! Session details loaded")
        print(f"\n   User: {data.get('user_name')}")
        print(f"   Test Number: {data.get('test_number')}")
        print(f"   Score: {data.get('score')}")
        print(f"   Percentage: {data.get('percentage'):.1f}%")
        print(f"   Status: {'Bestanden ✓' if data.get('passed') else 'Nicht bestanden ✗'}")
        print(f"   Mistakes Found: {len(data.get('mistakes', []))}")
        
        answers = data.get('answers_json', {})
        if answers.get('schreiben'):
            brief = answers['schreiben']
            if isinstance(brief, dict):
                brief_text = brief.get('text', '')
            else:
                brief_text = str(brief)
            word_count = len(brief_text.split())
            print(f"   Brief: {word_count} words")
        
        print("\n   Teil scores:")
        print(f"   - Teil 1: {data.get('teil1_score', 0)}/20")
        print(f"   - Teil 2: {data.get('teil2_score', 0)}/10")
        print(f"   - Teil 3: {data.get('teil3_score', 0)}/15")
        print(f"   - Teil 4: {data.get('teil4_score', 0)}/10")
        
        # Show first few mistakes
        mistakes = data.get('mistakes', [])
        if mistakes:
            print(f"\n   First 3 mistakes:")
            for m in mistakes[:3]:
                print(f"   - Q{m.get('question_id')}: {m.get('question_text')[:50]}...")
        
    except Exception as e:
        print(f"❌ Error loading details: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_details_endpoint()
