@echo off

echo pip install requests > temp.bat
echo exit >> temp.bat

start cmd /c temp.bat

timeout /t 10 /nobreak >nul

start cmd /c python spammer.py

del temp.bat