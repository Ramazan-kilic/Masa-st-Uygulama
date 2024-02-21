from PyQt5 import uic

with open("bilgi_Ekrani.py","w",encoding="utf-8") as pencere:
    uic.compileUi("bilgi_Ekrani.ui",pencere)