from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class pencere(QWidget):

    def __init__(self):
        super().__init__()
        self.islem=""
        self.setUI()
    def setUI(self):
        self.setWindowTitle("Nes'in Hesap Makinesi")
        self.yazi1 = QLabel("1.Sayı : ")
        self.yazi2 = QLabel("2.Sayı : ")
        self.sonuc = QLabel("Sonuç  burada yazılacaktır ! ")
        self.temizle=QPushButton("Temizle")
        self.sonuc.setAlignment(Qt.AlignCenter)

        self.giris1=QLineEdit()
        self.giris2 = QLineEdit()

        self.topla=QPushButton("+")
        self.cikar=QPushButton("-")
        self.carp=QPushButton("x")
        self.bol=QPushButton("/")

        self.yazi1.setFont(QFont("Arial", 10, QFont.Bold))
        self.yazi2.setFont(QFont("Arial", 10, QFont.Bold))
        self.giris1.setFont(QFont("Arial", 10, QFont.Bold))
        self.giris2.setFont(QFont("Arial", 10, QFont.Bold))
        self.temizle.setFont(QFont("Arial", 10, QFont.Bold))
        self.sonuc.setFont(QFont("Arial", 10, QFont.Bold))
        self.topla.setFont(QFont("Arial",10,QFont.Bold))
        self.cikar.setFont(QFont("Arial",10,QFont.Bold))
        self.carp.setFont(QFont("Arial",10,QFont.Bold))
        self.bol.setFont(QFont("Arial",10,QFont.Bold))



        self.buton=QPushButton("Hesapla")
        self.buton.setFont(QFont("Arial", 10, QFont.Bold))
        h_box1=QHBoxLayout()
        h_box_islemler=QHBoxLayout()
        h_box_islemler.addWidget(self.topla)
        h_box_islemler.addWidget(self.cikar)
        h_box_islemler.addWidget(self.carp)
        h_box_islemler.addWidget(self.bol)
        h_box2 = QHBoxLayout()

        h_box1.addWidget(self.yazi1)
        h_box1.addWidget(self.giris1)

        h_box2.addWidget(self.yazi2)
        h_box2.addWidget(self.giris2)

        v_box=QVBoxLayout()

        v_box.addLayout(h_box1)
        v_box.addLayout(h_box_islemler)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.sonuc)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.buton)

        self.topla.clicked.connect(self.Topla)
        self.cikar.clicked.connect(self.Cikar)
        self.carp.clicked.connect(self.Carp)
        self.bol.clicked.connect(self.Bol)

        self.buton.clicked.connect(self.uygula)
        self.temizle.clicked.connect(self.Temizle)


        self.setLayout(v_box)
        self.show()

    def Temizle(self):
        self.giris1.clear()
        self.giris2.clear()

    def Topla(self):
        self.islem="+"
    def Cikar(self):
        self.islem = "-"
    def Carp(self):
        self.islem = "x"
    def Bol(self):
        self.islem = "/"

    def uygula(self):
        if self.islem=="+":
            try:
                giris1 = int(self.giris1.text())
                giris2 = int(self.giris2.text())
                sonuc=giris1+giris2
                self.sonuc.setText(str(sonuc))
            except ValueError:
                self.giris1.clear()
                self.giris1.clear()
        elif self.islem=="-":
            try:
                giris1 = int(self.giris1.text())
                giris2 = int(self.giris2.text())
                sonuc=giris1-giris2
                self.sonuc.setText(str(sonuc))
            except ValueError:
                self.giris1.clear()
                self.giris1.clear()
        elif self.islem=="x":
            try:
                giris1 = int(self.giris1.text())
                giris2 = int(self.giris2.text())
                sonuc=giris1*giris2
                self.sonuc.setText(str(sonuc))
            except ValueError:
                self.giris1.clear()
                self.giris1.clear()
        elif self.islem=="/":
            try:
                giris1 = float(self.giris1.text())
                giris2 = float(self.giris2.text())
                sonuc=giris1/giris2
                self.sonuc.setText(str(sonuc))
            except ValueError:
                self.giris1.clear()
                self.giris1.clear()



if __name__ =="__main__":
    app=QApplication(sys.argv)
    pencere=pencere()
    sys.exit(app.exec())