@echo off
title Detectum-OSINT - Advanced OSINT Investigation Tool
color 0A

echo.
echo ========================================
echo    DETECTUM-OSINT - Windows Utility
echo ========================================
echo    Developed by Vishal Coodye
echo    Detectum Cybersecurity, Republic of Mauritius
echo ========================================
echo.

if "%1"=="" (
    echo Usage: detectum-osint.bat username
    echo.
    echo Examples:
    echo   detectum-osint.bat john_doe
    echo   detectum-osint.bat jane_smith
    echo.
    echo For more options, run: python detectum_osint.py --help
    echo.
    pause
    exit /b 1
)

echo Starting investigation for username: %1
echo.
echo This will check multiple platforms for account existence...
echo Estimated time: 2-5 minutes depending on network speed
echo.
echo Press Ctrl+C to cancel at any time
echo.

python detectum_osint.py %1

echo.
echo ========================================
echo Investigation completed for: %1
echo ========================================
echo.
echo Results have been displayed above.
echo To save results to a file, use:
echo   python detectum_osint.py %1 -f results.txt
echo.
pause
