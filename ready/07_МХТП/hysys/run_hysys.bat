@echo off
chcp 65001 >nul
cd /d "%~dp0"
python hysys_auto.py %*
pause
