@echo off
cd /d "%~dp0"

if exist venv\Scripts\activate (
    call venv\Scripts\activate
) else (
    echo Virtual environment not found in venv\Scripts\activate
    echo Attempting to run without virtual environment...
)

echo Starting Django Server...
python manage.py runserver 0.0.0:8000

pause
