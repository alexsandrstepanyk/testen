#!/usr/bin/env python3
import re, sys, subprocess

with open('../frontend/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ('.screen{display:none;opacity:0', 'screen base has opacity:0'),
    ('.screen.active{display:block;opacity:1;transform:none;}', 'screen.active fix present'),
    ('screenIn', 'screenIn keyframe present'),
    ('screenOut', 'screenOut keyframe present'),
    ('burstConfetti', 'confetti function present'),
    ('goToFirstUnanswered', 'jump-to-unanswered present'),
    ('initMotionFX', 'motion FX present'),
    ('initClickRipples', 'ripple FX present'),
    ('bindCardTilt', 'card tilt present'),
    ('prefers-reduced-motion', 'reduced motion support present'),
    ('scr(', 'animated scr() function present'),
    ('setTeil', 'setTeil function present'),
    ('doSubmit', 'doSubmit function present'),
    ('resultMorph', 'resultMorph animation present'),
    ('optIn', 'optIn stagger animation present'),
    ('confettiFall', 'confettiFall animation present'),
    ('focusPulse', 'focusPulse animation present'),
]

print('=== CSS/JS integrity checks ===')
all_ok = True
for needle, label in checks:
    found = needle in html
    status = 'OK  ' if found else 'MISS'
    if not found:
        all_ok = False
    print(f'  [{status}] {label}')

# Tag balance
scripts_open = len(re.findall(r'<script', html))
scripts_close = len(re.findall(r'</script>', html))
styles_open = len(re.findall(r'<style', html))
styles_close = len(re.findall(r'</style>', html))

print(f'\n=== Tag balance ===')
print(f'  <script>  : {scripts_open} open, {scripts_close} close  {"OK" if scripts_open==scripts_close else "MISMATCH!"}')
print(f'  <style>   : {styles_open} open, {styles_close} close  {"OK" if styles_open==styles_close else "MISMATCH!"}')

# Critical screens
screens = ['scStart','scTest','scResult','scRanking']
print(f'\n=== Screen divs ===')
for sc in screens:
    found = f'id="{sc}"' in html
    print(f'  [{"OK  " if found else "MISS"}] #{sc}')

# Check DOMContentLoaded calls
dom_calls = re.findall(r'addEventListener\(["\']DOMContentLoaded', html)
print(f'\n=== DOMContentLoaded listeners: {len(dom_calls)} ===')

print(f'\nHTML size: {len(html):,} bytes')
print('\n=== RESULT:', 'ALL CHECKS PASSED' if all_ok else 'SOME CHECKS FAILED', '===')
