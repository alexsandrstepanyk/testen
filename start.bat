@echo off
echo.
echo  ============================================
echo   Deutsch B1 Uebungstest — Server Start
echo  ============================================
echo.

cd /d "%~dp0backend"

echo [1/3] Prüfe Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo FEHLER: Python nicht gefunden!
    echo Bitte Python 3.10+ installieren: https://python.org
    pause
    exit /b 1
)

echo [2/3] Installiere Abhängigkeiten...
pip install -r requirements.txt --quiet

echo [3/3] Starte Server...
echo.
echo  Backend:  http://localhost:8000
echo  Frontend: http://localhost:8000
echo  API Docs: http://localhost:8000/docs
echo  Rangliste wird automatisch gespeichert.
echo.
echo  Drücken Sie Ctrl+C zum Beenden.
echo.

python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
pause
