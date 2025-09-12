@echo off
echo Business Strategy Quiz Week Creator
echo ===================================

if "%1"=="" (
    echo Usage: create_week.bat [week_number]
    echo Example: create_week.bat 2
    exit /b 1
)

python create_week.py %1

if %ERRORLEVEL% == 0 (
    echo.
    echo SUCCESS: Week %1 structure created!
    echo You can now:
    echo - Add quiz screenshots to week_%1/quiz_questions/
    echo - Fill in answers in week_%1/quiz_answers.md
) else (
    echo ERROR: Failed to create week structure
)

pause