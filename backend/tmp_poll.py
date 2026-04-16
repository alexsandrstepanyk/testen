#!/usr/bin/env python3
import urllib.request, time, sys

url = 'https://deutsch-b1-app.onrender.com/'
needle = '.screen.active{display:block;opacity:1;transform:none;}'
attempts = 0
max_attempts = 24  # 24 x 15s = 6 minutes

print('Polling production for new deployment...', flush=True)
while attempts < max_attempts:
    attempts += 1
    try:
        req = urllib.request.Request(url, headers={'Cache-Control':'no-cache','Pragma':'no-cache'})
        with urllib.request.urlopen(req, timeout=30) as r:
            html = r.read().decode('utf-8','ignore')
        size = len(html)
        has_fix = needle in html
        has_confetti = 'burstConfetti' in html
        print(f'  [{attempts:02d}] size={size:,} fix={has_fix} confetti={has_confetti}', flush=True)
        if has_fix and has_confetti:
            print('\nSUCCESS! New version is live on production.')
            sys.exit(0)
    except Exception as e:
        print(f'  [{attempts:02d}] error: {e}', flush=True)
    time.sleep(15)

print('\nTimeout - deploy still in progress. Check Render dashboard.')
sys.exit(1)
