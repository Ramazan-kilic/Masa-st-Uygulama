from bilgi_Ekrani import *
from giris_paneli import *
from menu import *
from kayit_ekrani import *
from PyQt5.QtWidgets import *
import sqlite3
import sys

con = sqlite3.connect("masaüstü_uygulam.db")
crsr=con.cursor()
class giris_paneli(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=login_Screen()
        self.ui.setupUi(self)
        self.ui.btn_giris.clicked.connect(self.giris_kontrol)

    def giris_kontrol(self, ):
        ka = self.ui.txt_ka.text()
        sfr =self.ui.txt_sfr.text()
        crsr.execute(f"select * from kullanıcılar where kullanıcı_adı='{ka}' and kullanıcı_sifre='{sfr}'")
        kisi=crsr.fetchone()
        if kisi:
            QMessageBox.information(None," Bilgi","Giriş Başarılı")
            self.hide()
            self.menu=menu()
            self.menu.show()
        else:
            QMessageBox.critical(None," Bilgi","Giriş Başarısız")



class menu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Menu_Screen()
        self.ui.setupUi(self)
        self.ui.btn_personel_ekle.clicked.connect(self.personel_ekle)
        self.ui.btn_ogrenci_bilgileri.clicked.connect(self.personel_bilgi)
    def personel_ekle(self):
        self.hide()
        self.prs_ekle= kayit_ekrani()
        self.prs_ekle.show()
    def personel_bilgi(self):
        self.hide()
        self.prs_bilgi = bilgi_Ekranı()
        self.prs_bilgi.show()
class kayit_ekrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_kayit_ekrani()
        self.ui.setupUi(self)
        self.ui.btn_kaydet.clicked.connect(self.personel_kayıt)
        self.kayit_ekrani.show()
    def personel_kayıt(self):
        ad = self.ui.txt_ad_kayit.text()
        soyad = self.ui.txt_soyad_kayit.text()
        tc = self.ui.txt_tc_kayit.text()
        dogum_yeri=self.ui.cmb_il_kayit.currentText()
        dogum_tarihi=self.ui.dt_tarih_kayit.date().toString("yyyy-MM-dd")
        global cinsiyet
        if self.ui.rd_erkek_kayit.isEnabled():
            cinsiyet = self.ui.rd_erkek_kayit.text()
        else:
            self.ui.rd_kadin_kayit.text()
        crsr.execute(f"İnsert İnto Personel (f'AD'.'SOYAD'.'TC'.'Dogum_yeri','Dogum_tarihi') values ('{ad}.'{soyad},'{tc},'{cinsiyet}','{dogum_yeri},'{dogum_tarihi}') ")
        con.commit()




class bilgi_Ekranı(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Bilgi_Ekrani()
        self.ui.setupUi(self)
        self.HerkesiGetir()
        self.ui.btn_ara.clicked.connect(self.aramayap)
        self.ui.tbl_ogrenci.cellClicked.connect(self.Hucreverial)

    def HerkesiGetir(self):
        crsr.execute("Select * from Personel")
        veriler=crsr.fetchall()
        #description = crsr.description
        baslıklar=[baslık[0] for baslık in crsr.description]
        self.ui.tbl_ogrenci.verticalHeader().setVisible(False)
        self.ui.tbl_ogrenci.setRowCount(len(veriler))
        self.ui.tbl_ogrenci.setColumnCount(len(veriler[0]))

        for sutun_sayısı,baslık in enumerate(baslıklar):
            item=QTableWidgetItem(baslık)
            self.ui.tbl_ogrenci.setHorizontalHeaderItem(sutun_sayısı,item)

        for satır_sayısı,satır_verileri in enumerate(veriler):
            for sutun_sayısı,kisi_verisi in enumerate(satır_verileri):
                item=QTableWidgetItem(str(kisi_verisi))
                self.ui.tbl_ogrenci.setItem(satır_sayısı,sutun_sayısı,item)

    def aramayap(self):
        if (self.ui.txt_tc_bilgi.strip==""):
            crsr.execute("Select * from Personel")
            veriler = crsr.fetchall()
            self.ui.tbl_ogrenci.setRowCount(len(veriler))
            self.ui.tbl_ogrenci.setColumnCount(len(veriler[0]))

            for satır_sayısı, satır_verileri in enumerate(veriler):
                for sutun_sayısı, kisi_verisi in enumerate(satır_verileri):
                    item = QTableWidgetItem(str(kisi_verisi))
                    self.ui.tbl_ogrenci.setItem(satır_sayısı, sutun_sayısı, item)
        else:
            tc = self.ui.txt_tc_bilgi.text()
            crsr.execute(f"Select * From Personel where TC ='{tc}'")
            kisi = crsr.fetchall()
            self.ui.tbl_ogrenci.setRowCount(len(kisi))
            self.ui.tbl_ogrenci.setColumnCount(len(kisi[0]))

            for satır_sayısı, satır_verileri in enumerate(kisi):
                for sutun_sayısı, kisi_verisi in enumerate(satır_verileri):
                    item = QTableWidgetItem(str(kisi_verisi))
                    self.ui.tbl_ogrenci.setItem(satır_sayısı, sutun_sayısı, item)

            self.ui.txt_tc_bilgi.clear()

    def Hucreverial(self,satir):
        satir_verisi=[]
        for i in range(self.ui.tbl_ogrenci.columnCount()):
            item = self.ui.tbl_ogrenci.item(satir,i)
            if item is not None:
                satir_verisi.append(item.text())
            else:
                satir_verisi.append(None)
        self.ui.txt_id_bilgi.setText(satir_verisi[0])
        self.ui.txt_ad_bilgi.setText(satir_verisi[1])
        self.ui.txt_soyad_bilgi.setText(satir_verisi[2])
        self.ui.btn_guncelle.setText(satir_verisi[3])
        self.ui.cmb_il_bilgi.setCurrentText(satir_verisi[5])
        self.ui.dt_tarih_bilgi.setSpecialValueText(satir_verisi[6])

def Uygulama():
    app = QApplication(sys.argv)
    pencere = giris_paneli()
    pencere.show()
    sys.exit(app.exec())


if __name__== "__main__":
    Uygulama()