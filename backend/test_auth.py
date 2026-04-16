#!/usr/bin/env python3
import urllib.request, json, base64

# Тест 1: БЕЗ аутентифікації (як робить фронтенд)
print("=== Тест 1: БЕЗ auth (як фронтенд) ===")
try:
    req = urllib.request.Request('https://deutsch-b1-app.onrender.com/api/teacher/sessions/55/details')
    resp = urllib.request.urlopen(req, timeout=20)
    print(f"✅ Status: {resp.status}")
except urllib.error.HTTPError as e:
    print(f"❌ HTTP {e.code}")
    error_msg = e.read().decode()
    print(f"   Message: {error_msg[:300]}")
except Exception as e:
    print(f"❌ Error: {e}")

print("\n=== Тест 2: З auth (як admin) ===")
try:
    req = urllib.request.Request('https://deutsch-b1-app.onrender.com/api/teacher/sessions/55/details')
    req.add_header('Authorization', 'Basic ' + base64.b64encode(b'admin:admin').decode())
    resp = urllib.request.urlopen(req, timeout=20)
    data = json.loads(resp.read())
    print(f"✅ Status: {resp.status}")
    print(f"✅ Data received: mistakes={len(data.get('mistakes', []))}")
except urllib.error.HTTPError as e:
    print(f"❌ HTTP {e.code}")
    error_msg = e.read().decode()
    print(f"   Message: {error_msg[:300]}")
except Exception as e:
    print(f"❌ Error: {e}")
