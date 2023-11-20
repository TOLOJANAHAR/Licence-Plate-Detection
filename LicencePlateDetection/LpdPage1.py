import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIcon
import mysql.connector
from LpdPage2 import MaFenetrePrincipale1
from LpdPage0 import MaFenetrePrincipale0

class MaFenetrePrincipale(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # #plate
        Plate = QLabel(self)
        pixmap = QPixmap("plate.png")
        Plate.setPixmap(pixmap)
        Plate.setStyleSheet("""width: 80px; height: 40px;margin-left: 100px;""")
        Plate.setFixedSize(200, 40)
        #se connecter
        seconnecter = QLabel('Bienvenue')
        seconnecter.setStyleSheet("""color: #FFF; font-family: Prompt; font-size: 28px; font-weight: 600;line-height: normal; font-style: normal; margin-left: 260px;""")
        seconnecter.setFixedSize(470, 25)
        #explication
        explication = QLabel('Connecter a votre compte Plate')
        explication.setStyleSheet("""color: #A1A1A1; font-family: Prompt; font-size: 15px; font-weight: 400; line-height: normal; font-style: normal;margin-left: 220px;""")
        explication.setFixedSize(600, 15)
        #input mdp
        self.input_field = QLineEdit()
        self.input_field.setEchoMode(QLineEdit.Password)
        self.input_field.setStyleSheet("""border-radius:0px;border: 1px solid #575757;background: #FFF;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 10px;margin-left: 100px;""")
        self.input_field.setFixedSize(600, 55)
        self.input_field.setPlaceholderText("Mot de passe")
        #input contact
        self.input_Contact = QLineEdit()
        self.input_Contact.setStyleSheet("""border-radius:0px;border: 1px solid #575757;background: #FFF;color: #2E3739;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 10px;margin-left: 95px""")
        self.input_Contact.setFixedSize(280, 55)
        self.input_Contact.setPlaceholderText("Contact")
        #input mail
        self.input_Mail = QLineEdit()
        self.input_Mail.setStyleSheet("""border-radius:0px;border: 1px solid #575757;background: #FFF;color: #2E3739;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 10px;margin-left: 10px;""")
        self.input_Mail.setFixedSize(310, 55)
        self.input_Mail.setPlaceholderText("Email")
        #connexion
        self.Connexion = QPushButton('Connexion')
        self.Connexion.setStyleSheet("""border-radius: 0px;background: #534FFF;width: 470px;height: 44px;color: #FFF;font-family: Prompt;font-size: 15px;font-style: normal;font-weight: 700;line-height: normal;margin-left: 100px;""")
        self.Connexion.setFixedSize(600, 55)
        self.Connexion.clicked.connect(self.login)
        #texteConnexion
        self.textConnexion = QPushButton('Pas encore de compte? Creer un Compte')
        self.textConnexion.setStyleSheet("""color: #A1A1A1; font-family: Prompt; font-size: 12px; font-weight: 400; line-height: normal; font-style: normal;margin-left: 130px; border: tranparent;""")
        self.textConnexion.setFixedSize(600, 15)
        self.textConnexion.clicked.connect(self.goToPage0)


        #image
        Image = QLabel(self)
        pixmap = QPixmap("im.png")
        Image.setPixmap(pixmap)
        Image.setStyleSheet("""width: 1000px; height: 100px; padding-top: 20px;margin-left: 80px;""")
        Image.setFixedSize(1050, 800)

        layoutD = QVBoxLayout()
        layoutD.addWidget(Image)

        layoutG = QVBoxLayout()
        layoutIn = QHBoxLayout()
        layoutIn.addWidget(self.input_Contact)
        layoutIn.addWidget(self.input_Mail)
        layoutG.addWidget(Plate)
        layoutG.addWidget(seconnecter)
        layoutG.addSpacing(-115)
        layoutG.addWidget(explication)
        layoutG.addSpacing(-110)
        layoutG.addLayout(layoutIn)
        layoutG.addSpacing(-110)
        layoutG.addWidget(self.input_field)
        layoutG.addSpacing(-110)
        layoutG.addWidget(self.Connexion)
        layoutG.addSpacing(-120)
        layoutG.addWidget(self.textConnexion)
        layoutG.setContentsMargins(0, 0, 100, 100)

        layout = QHBoxLayout()
        layout.addLayout(layoutG)
        layout.addLayout(layoutD)
        self.setLayout(layout)

        self.setWindowTitle('Log In')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(0, 0, 1900, 1000)
        self.setContentsMargins(50, 40, 0, 100)
        self.setStyleSheet("background: #05161F;")

    def button_click(self):
        print('Le bouton a été cliqué!')

    def login(self):
        phone = self.input_Contact.text()
        phone = int(phone)
        password = self.input_field.text()
        email = self.input_Mail.text()

        if phone and password and email:
            db = mysql.connector.connect(
                host="localhost",  
                user="root",  
                password="",  
                database="plate" 
            )

            cursor = db.cursor()
            query = "SELECT * FROM user WHERE Contact = %s AND MotDePasse = %s AND Mail = %s"
            values = (phone, password, email)
            cursor.execute(query, values)
            result = cursor.fetchone()
            if result:
                print("Connexion réussie.")
                self.goToPage2()
            else:
                print("Échec de la connexion. Vérifiez vos informations.")
            
            cursor.close()
            db.close()
        else:
            print("Veuillez remplir tous les champs.")

    def goToPage2(self):
        self.LpdPage2 = MaFenetrePrincipale1()  
        self.LpdPage2.show() 
        self.hide() 

    def goToPage0(self):
        self.LpdPage0 = MaFenetrePrincipale0()  
        self.LpdPage0.show() 
        self.hide() 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetrePrincipale()
    fenetre.show()
    sys.exit(app.exec_())


   
