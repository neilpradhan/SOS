@echo off

REM Open terminal for encryption_server with venv creation and activation
start cmd /k "cd encryption_server && (if not exist .venv python -m venv .venv) && .venv\Scripts\activate && pip install -r requirements.txt"

REM Open terminal for decryption_server with venv creation and activation
start cmd /k "cd decryption_server && (if not exist .venv python -m venv .venv) && .venv\Scripts\activate && pip install -r requirements.txt"

REM Open terminal for encryption-app
start cmd /k "cd encryption_app && npm install"

REM Open terminal for decryption-app
start cmd /k "cd decryption_app && npm install"
