@echo off
REM Check if the virtual environment directory exists
IF NOT EXIST venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate the virtual environment
call venv\Scripts\activate

REM Install the requirements
if exist requirements.txt (
    echo Installing requirements...
    pip install -r requirements.txt
) else (
    echo requirements.txt not found.
)

REM Run the run.py script
if exist run.py (
    echo Running run.py...
    python run.py
) else (
    echo run.py not found.
)

REM Deactivate the virtual environment
deactivate

pause
