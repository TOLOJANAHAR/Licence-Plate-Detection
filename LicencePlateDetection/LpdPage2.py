import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QLineEdit, QFrame, QFileDialog, QTextEdit, QGraphicsBlurEffect, QComboBox
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import QEasingCurve
from PyQt5 import QtCore 
from PyQt5.QtGui import QPixmap, QIcon,QPainter, QImage,QColor
from QSwitchControl import SwitchControl
from LpdPage3 import MaFenetrePrincipale2
import subprocess
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pathlib import Path
import requests



class MaFenetrePrincipale1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # #plate
        Image = QLabel(self)
        pixmap = QPixmap("plate.png")
        Image.setPixmap(pixmap)
        Image.setStyleSheet("""width: 80px; height: 40px; padding-left: 50px;""")
        Image.setFixedSize(180, 40)



        #text1
        texte1 = QTextEdit('Obtenez facilement des informations de voiture avec Plate')
        texte1.setStyleSheet("""border: 2px solid #05161F;color: #FFF;font-family: Monument Extended;font-size: 55px;font-style: normal;font-weight: 850;line-height: normal;width: 914px;height: 128px;""")
        texte1.setAlignment(Qt.AlignCenter) 
        texte1.setFixedSize(1330, 150)
        #text2
        texte2 = QTextEdit('Un outil qui utilise une intelligence artificiel pour indentifier et chercher une plaque d\'imatriculation')
        texte2.setStyleSheet("""border: 2px solid #05161F;color: #A5A5A5;text-align: center;font-family: Prompt;font-size: 20px;font-style: normal;font-weight: 400;line-height: normal;margin-left: 50px;""")
        texte2.setAlignment(Qt.AlignCenter) 
        texte2.setFixedSize(1300, 70)
        #text3
        texte3 = QLabel('')
        texte3.setFixedSize(400, 180)
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(250)  
        texte3.setGraphicsEffect(blur)
        texte3.setStyleSheet("background-color: rgba(33, 252, 199, 1.0); margin-top: -100px; border-radius: 200px;")
        #text4
        texte4= QLabel('')
        texte4.setFixedSize(900, 300)
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(200)  
        texte4.setGraphicsEffect(blur)
        texte4.setStyleSheet("background-color: rgba(8, 25, 181, 1.0);border-radius: 100px;")


        #texteimage
        texteImage = QLabel('         VotreImageSelectionner.png')
        texteImage.setStyleSheet("""border: 2px solid #000 ;background: #D9D9D9;color: #2E3739;text-align: center;font-family: Prompt;font-size: 15px;font-style: normal;font-weight: 600;line-height: normal;""")
        texteImage.setFixedSize(335, 60)
        #bouton Bouton
        Bouton = QPushButton(' Bouton Image')
        Bouton.setStyleSheet("""border: 2px solid #000;background: #000;color: #FFF;text-align: center;font-family: Prompt;font-size: 15px;font-style: normal;font-weight: 400;line-height: normal;""")
        iconBouton = QIcon("poly.png")
        Bouton.setIcon(iconBouton)
        Bouton.setIconSize(QSize(30,30))
        Bouton.setFixedSize(180, 60)
        Bouton.clicked.connect(self.openImage)


        #Propos
        self.propos = QComboBox(self)
        self.propos.addItem('A propos')
        self.propos.addItem(' Plate est une application de détection de \n plaque d\'immatriculation,  alimentée par \n une puissante intelligence artificielle, \n a pour objectif de simplifier  la gestion \n du trafic et d\'améliorer la sécurité \n . En utilisant des algorithmes \n avancés de vision par ordinateur, \n elle peut rapidement et précisément lire \n les plaques d\'immatriculation, facilitant \n ainsi le suivi des véhicules, la gestion \n des parkings et la lutte \n contre la criminalité routière.')
        self.propos.setStyleSheet("""color: #D9D9D9;font-family: Prompt;font-size: 14px;font-style: normal;font-weight: 400;line-height: normal; border: 1px solid #05161F;""")
        self.propos.setFixedSize(300, 30)
        self.propos.activated.connect(self.retablirTexte)
        #support
        self.Support = QComboBox(self)
        mailIcon = QIcon('mail.png')
        whatsAppIcon = QIcon('WhatsApp.png')
        self.Support.addItem('Support')
        self.Support.addItem(whatsAppIcon, ' 034 32 606 86 ')
        self.Support.addItem(mailIcon, ' plate@gmail.com ')
        self.Support.setStyleSheet("""color: #D9D9D9;font-family: Prompt;font-size: 14px;font-style: normal;font-weight: 400;line-height: normal; border: 1px solid #05161F;""")
        self.Support.activated.connect(self.retablirTexte)
        self.Support.setFixedSize(150, 30)
        #Profil
        self.Profil = QComboBox(self)
        userIcon = QIcon('user.png')
        self.Profil.addItem('Profil')
        self.Profil.addItem(userIcon, 'Natacha')
        self.Profil.addItem(whatsAppIcon, '034 32 606 86')
        self.Profil.addItem(mailIcon, 'natacha@gmail.com')
        self.Profil.setStyleSheet("""color: #D9D9D9;font-family: Prompt;font-size: 14px;font-style: normal;font-weight: 400;line-height: normal; border: 1px solid #05161F;""")
        self.Profil.activated.connect(self.retablirTexte)
        self.Profil.setFixedSize(150, 30)

        #layout Page
        layoutPage = QHBoxLayout()

        #layout navigation
        layoutNav = QVBoxLayout()
        layoutNav.setContentsMargins(0, -300, 100, 400)
        layoutNavTop = QVBoxLayout()   
        layoutNavTop.addWidget(Image)
        layoutNavTop.addSpacing(800)
        layoutNav.addLayout(layoutNavTop)
        layoutPage.addLayout(layoutNav)
        #layout Menu
        layoutMenu = QVBoxLayout()
        layoutMenu.setContentsMargins(0, 0, 0, 80)
        layoutMenuTop = QHBoxLayout()
        layoutMenuTop.addSpacing(700)
        layoutMenuTop.addWidget(self.Profil)
        layoutMenuTop.addWidget(self.Support)
        layoutMenuTop.addWidget(self.propos)
        layoutMenuTop.setContentsMargins(0, 0, 0, 150)

        layoutMenuBottom = QHBoxLayout()

        layoutMenuBottomD = QVBoxLayout()
        layoutMenuBottomD.setContentsMargins(0, 30, 0, 200)
        layoutMenuBottomDH = QVBoxLayout()
        layoutMenuBottomDH.addWidget(texte1)
        layoutMenuBottomDH.addSpacing(-20)
        layoutMenuBottomDH.addWidget(texte2)
        layoutMenuBottomDB = QHBoxLayout()
        layoutMenuBottomDB.addWidget(texteImage)
        layoutMenuBottomDB.addSpacing(-420)
        layoutMenuBottomDB.addWidget(Bouton)
        layoutMenuBottomG = QHBoxLayout()
        layoutMenuBottomG.addWidget(texte4)
        layoutMenuBottomG.addSpacing(-1000)
        layoutMenuBottomG.addWidget(texte3)
        layoutMenuBottomD.addLayout(layoutMenuBottomDH)
        layoutMenuBottomD.addLayout(layoutMenuBottomDB)
        layoutMenuBottomD.addSpacing(100)
        layoutMenuBottomD.addLayout(layoutMenuBottomG)
        layoutMenuBottom.addLayout(layoutMenuBottomD)

        layoutMenu.addLayout(layoutMenuTop)
        layoutMenu.addLayout(layoutMenuBottom)
        layoutPage.addLayout(layoutMenu)
    
        self.setLayout(layoutPage)
        self.setWindowTitle('Licence Plate Recognation')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(0,0, 1900,500)
        self.setContentsMargins(30, 40, 250, 10)
        self.setStyleSheet("background: #05161F;")

    def goToPage2(self):
        from LpdPage3 import MaFenetrePrincipale2
        self.LpdPage3 = MaFenetrePrincipale2()
        self.LpdPage3.show()
        self.hide()  

    def retablirTexte(self, index):
        if index != 0:
            self.Profil.setCurrentIndex(0)
            self.propos.setCurrentIndex(0)
            self.Support.setCurrentIndex(0)

    
    def openImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        filePath, _ = QFileDialog.getOpenFileName(self, "Ouvrir une image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif *.tiff)", options=options)
        
        if filePath:
            image_path = Path(filePath)
            response = requests.post("http://127.0.0.1:8000/store_image_url/", json={"path": str(image_path)})
            if response.status_code == 200:
                print("Image URL stored successfully")
                pixmap = QPixmap(filePath)
                print(filePath)
            else:
                print("Failed to store the image URL")
        notebook_path = "E:/Projet/LPD/FileTrainingDetection.ipynb"
        process = subprocess.Popen(["jupyter", "nbconvert", "--execute", "--to", "notebook", notebook_path])
        process.wait()
        self.goToPage2()

    def loading(self):
        from loading import LoadingWindow
        self.loading = LoadingWindow()
        self.loading.show()
        self.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetrePrincipale1()
    fenetre.show()
    sys.exit(app.exec_())


   
