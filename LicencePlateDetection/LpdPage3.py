import sys
from PyQt5.QtWidgets import QApplication,QTextEdit, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QLineEdit, QFrame, QComboBox, QGraphicsBlurEffect
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import QEasingCurve
from PyQt5 import QtCore 
from PyQt5.QtGui import QPixmap, QIcon
from QSwitchControl import SwitchControl
import httpx

class MaFenetrePrincipale2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #plate
        Image = QLabel(self)
        pixmap = QPixmap("plate.png")
        Image.setPixmap(pixmap)
        Image.setStyleSheet("""width: 80px; height: 40px; padding-left: 50px;""")
        Image.setFixedSize(180, 40)

        #retour
        Bouton = QPushButton('')
        Bouton.setStyleSheet("""border: 2px solid transparent;background: #05161F;color: #FFF;text-align: center;font-family: Prompt;font-size: 15px;font-style: normal;font-weight: 400;line-height: normal;""")
        iconBouton = QIcon("fleche.png")
        Bouton.setIcon(iconBouton)
        Bouton.setIconSize(QSize(30,30))
        Bouton.setFixedSize(50, 50)
        Bouton.clicked.connect(self.retour)

        #Propos
        self.propos = QComboBox(self)
        self.propos.addItem('A propos')
        self.propos.addItem(' Plate est une application de détection de \n plaque d\'immatriculation,  alimentée par \n une puissante intelligence artificielle, \n a pour objectif de simplifier  la gestion \n du trafic et d\'améliorer la sécurité \n. En utilisant des algorithmes \n avancés de vision par ordinateur, \n elle peut rapidement et précisément lire \n les plaques d\'immatriculation, facilitant \n ainsi le suivi des véhicules, la gestion \n des parkings et la lutte \n contre la criminalité routière.')
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

        #API
        api_url = "http://localhost:8000/get_list"
        response = httpx.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                data_list = data[0] 
                id = data_list[0]
                adresse = data_list[1]
                coorEnregistrer = data_list[2]
                coorActuel = data_list[3]
                etatVoiture = data_list[4]
                mandatCours = data_list[5]
                condamnation = data_list[6]
                activiteCrim = data_list[7]
                assurance = data_list[8]
                dateAssurance = data_list[9]
                dateAssurancePlice = data_list[10]
                accident = data_list[11]
                infractionCirculaire = data_list[12]
                conduiteDanze = data_list[13]
                stationnement = data_list[14]
                contravention = data_list[15]
                amandePayer = data_list[16]
                impot = data_list[17]
                taxe = data_list[18]
                nom = data_list[19]
                texte1 = QLabel("IM : " + id)
                inputNomPropriete = QLabel('Nom du propriete : ' + nom)
                adresseProp = QLabel('Adresse du propriete : ' + adresse)
                coorEnregistrerProp = QTextEdit('Coordonee avant enregistrement du propriete : ' + coorEnregistrer)
                coorActuelProp = QLabel('Coordonee actuel du propriete : ' + coorActuel)
                etatVoitureProp = QLabel('Etat de la voiture : ' + etatVoiture)
                mandatCoursVoiture = QLabel('Mandat en cours : ' + mandatCours)
                condamnationVoiture = QLabel('Condamnation en cours :' + condamnation)
                activiteCrimVoiture = QLabel('Lier avec un activite criminel en cours : ' + activiteCrim)
                assuranceVoiture = QLabel('Assurance de la voiture : ' + assurance)
                dateAssuranceVoiture = QLabel('Date d\'assurance de la voiture : ' + dateAssurance)
                dateAssurancePliceVoiture = QLabel('Date d\'assurance Police de la voiture : ' + dateAssurancePlice)
                accidentVoiture = QLabel('Voiture lier a un accident : ' + accident)
                infractionCirculaireVoiture = QLabel('Detail d\'une infraction circulaire : ' + infractionCirculaire)
                conduiteDanzeVoiture = QLabel('Voiture lier a une conduite dangeureuse : ' + conduiteDanze)
                stationnementVoiture = QLabel('Voiture lier a une infraction de stantionement : ' + stationnement)
                contraventionVoiture = QLabel('Voiture lier a une contravention : ' + contravention)
                amandePayerVoiture = QLabel('Amande impayer : ' + amandePayer)
                impotVoiture = QLabel('Etat d\'impot : ' + impot)
                taxeVoiture = QLabel('Etat de taxe : ' + taxe)
                
                
            else:
                print ("error: Aucune donnée disponible")
        else:
            print ("Erreur : {response.status_code} - Impossible de récupérer la liste")

        #DROITE
        #mandatCoursVoiture
        mandatCoursVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        mandatCoursVoiture.setFixedSize(750, 70)
        #condamnationVoiture
        condamnationVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        condamnationVoiture.setFixedSize(750, 70)
        #activiteCrimVoiture
        activiteCrimVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        activiteCrimVoiture.setFixedSize(750, 70)
        #assuranceVoiture
        assuranceVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        assuranceVoiture.setFixedSize(750, 70)
        #dateAssuranceVoiture
        dateAssuranceVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        dateAssuranceVoiture.setFixedSize(750, 70)
        #dateAssuranceVoiture
        conduiteDanzeVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        conduiteDanzeVoiture.setFixedSize(750, 70)
        stationnementVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        stationnementVoiture.setFixedSize(750, 70)
        contraventionVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        contraventionVoiture.setFixedSize(750, 70)
        amandePayerVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        amandePayerVoiture.setFixedSize(750, 70)
        #accidentVoiture
        accidentVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        accidentVoiture.setFixedSize(750, 70)


        #GAUCHE
        #texte1
        texte1.setStyleSheet("""color: #FFF;font-family: Prompt;font-size: 28px;font-style: normal;font-weight: 750;line-height: normal; margin-left: 70px;""")
        texte1.setContentsMargins(0, 100, 0, 0)
        texte1.setFixedSize(350, 30)
        #inputNomPropriete
        inputNomPropriete.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 10px;margin-left: 70px;""")
        inputNomPropriete.setFixedSize(750, 70)
        #adresseProp
        adresseProp.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        adresseProp.setFixedSize(750, 70)
        #naissance
        naissance  = QLabel("Date de naissance : 11 Novembre 1969 ")
        naissance.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        naissance.setFixedSize(750, 70)
        #coorEnregistrerProp
        coorEnregistrerProp.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        coorEnregistrerProp.setFixedSize(750, 70)
        #coorActuelProp
        coorActuelProp.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        coorActuelProp.setFixedSize(750, 70)
        #etatVoitureProp
        etatVoitureProp.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        etatVoitureProp.setFixedSize(750, 70)
        #infractionCirculaireVoiture
        infractionCirculaireVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        infractionCirculaireVoiture.setFixedSize(750, 70)
        ##impotVoiture
        impotVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        impotVoiture.setFixedSize(750, 70)
        ##taxeVoiture
        taxeVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        taxeVoiture.setFixedSize(750, 70)
        ##dateAssurancePliceVoiture
        dateAssurancePliceVoiture.setStyleSheet("""border: 2px solid #534FFF;background: #D9D9D9;color: #05161F;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        dateAssurancePliceVoiture.setFixedSize(750, 70)

        texte3 = QLabel('')
        texte3.setFixedSize(400, 100)
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(250)  
        texte3.setGraphicsEffect(blur)
        texte3.setStyleSheet("background-color: rgba(33, 252, 199, 1.0); border-radius: 200px;")
        #text4
        texte4= QLabel('')
        texte4.setFixedSize(900, 140)
        blur = QGraphicsBlurEffect()
        blur.setBlurRadius(200)  
        texte4.setGraphicsEffect(blur)
        texte4.setStyleSheet("background-color: rgba(8, 25, 181, 1.0);border-radius: 100px;")



        #layout Page
        layoutPage = QHBoxLayout()
        #layout Menu
        layoutMenu = QVBoxLayout()
        layoutMenu.setContentsMargins(0, 0, 0, 0)

        layoutMenuTop = QHBoxLayout()
        layoutMenuTop.setContentsMargins(0, 0, 0, 50)
        layoutMenuTop.addWidget(Image)
        layoutMenuTop.addWidget(Bouton)
        layoutMenuTop.addSpacing(800)
        layoutMenuTop.addWidget(self.Profil)
        layoutMenuTop.addWidget(self.Support)
        layoutMenuTop.addWidget(self.propos)


        layoutMenuBottom = QHBoxLayout()
        layoutMenuBottom.setContentsMargins(0, 0, 0, 0)
        layoutMenuBottomD = QVBoxLayout()
        layoutMenuBottomD.addWidget(texte1)
        layoutMenuBottomD.addSpacing(10)
        layoutMenuBottomD.addWidget(inputNomPropriete)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(naissance)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(adresseProp)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(infractionCirculaireVoiture)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(coorEnregistrerProp)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(coorActuelProp)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(etatVoitureProp)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(conduiteDanzeVoiture)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(stationnementVoiture)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(contraventionVoiture)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.setContentsMargins(130, 0, 0, 120)

        layoutMenuBottomG = QVBoxLayout()
        layoutMenuBottomG.addWidget(mandatCoursVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.addWidget(amandePayerVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.addWidget(condamnationVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.addWidget(activiteCrimVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.addWidget(assuranceVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.addWidget(dateAssuranceVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.addWidget(dateAssurancePliceVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.addWidget(accidentVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.addWidget(impotVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.addWidget(taxeVoiture)
        layoutMenuBottomG.addSpacing(0)
        layoutMenuBottomG.setContentsMargins(0, 40, 0, 110)

        layoutMenuBottom.addLayout(layoutMenuBottomD)
        layoutMenuBottom.addLayout(layoutMenuBottomG)


        jayoutBlur = QHBoxLayout()
        jayoutBlur.addWidget(texte4)
        jayoutBlur.addSpacing(-1000)
        jayoutBlur.addWidget(texte3)
        layoutMenu.addLayout(layoutMenuTop)
        layoutMenu.addLayout(layoutMenuBottom)
        layoutMenu.addSpacing(-100)
        layoutMenu.addLayout(jayoutBlur)
        layoutPage.addLayout(layoutMenu)

        self.setLayout(layoutPage)
        self.setWindowTitle('Resultat')
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(0, 0, 1900, 1050)
        self.setContentsMargins(0, 40, 250, 0)
        self.setStyleSheet("background: #05161F;")
    def retablirTexte(self, index):
        if index != 0:
            self.Profil.setCurrentIndex(0)
            self.propos.setCurrentIndex(0)
            self.Support.setCurrentIndex(0)

    def retour(self):
        from LpdPage2 import MaFenetrePrincipale1
        self.LpdPage2 = MaFenetrePrincipale1()
        self.LpdPage2.show()
        self.hide()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetrePrincipale2()
    fenetre.show()
    sys.exit(app.exec_())


   
