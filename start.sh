#!/bin/bash
echo ""
echo " ============================================"
echo "  Deutsch B1 Übungstest — Server Start"
echo " ============================================"
echo ""

cd "$(dirname "$0")/backend"

echo "[1/3] Prüfe Python..."
if ! command -v python3 &>/dev/null; then
    echo "FEHLER: Python3 nicht gefunden!"
    echo "Bitte Python 3.10+ installieren: https://python.org"
    exit 1
fi

echo "[2/3] Installiere Abhängigkeiten..."
pip3 install -r requirements.txt --quiet

echo "[3/3] Starte Server..."
echo ""
echo " Backend:  http://localhost:8000"
echo " Frontend: http://localhost:8000"
echo " API Docs: http://localhost:8000/docs"
echo ""
echo " Drücken Sie Ctrl+C zum Beenden."
echo ""

python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
