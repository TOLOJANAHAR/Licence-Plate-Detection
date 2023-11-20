import sys
from PyQt5.QtWidgets import QApplication,QTextEdit, QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow, QHBoxLayout, QLineEdit, QFrame
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
        #text1
        texte1 = QTextEdit('Obtenez facilement des informations de voiture avec Plate')
        texte1.setStyleSheet("""border: 2px solid #05161F;color: #FFF;font-family: Monument Extended;font-size: 55px;font-style: normal;font-weight: 850;line-height: normal;width: 914px;height: 128px;""")
        texte1.setAlignment(Qt.AlignCenter) 
        texte1.setFixedSize(1330, 150)


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
        mandatCoursVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        mandatCoursVoiture.setFixedSize(550, 55)
        #condamnationVoiture
        condamnationVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        condamnationVoiture.setFixedSize(550, 55)
        #activiteCrimVoiture
        activiteCrimVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        activiteCrimVoiture.setFixedSize(550, 55)
        #assuranceVoiture
        assuranceVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        assuranceVoiture.setFixedSize(550, 55)
        #dateAssuranceVoiture
        dateAssuranceVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        dateAssuranceVoiture.setFixedSize(550, 55)
        #dateAssurancePliceVoiture
        dateAssurancePliceVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        dateAssurancePliceVoiture.setFixedSize(550, 55)
        #dateAssurancePliceVoiture
        accidentVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        accidentVoiture.setFixedSize(550, 55)
        #GAUCHE
        #texte1
        texte1.setStyleSheet("""color: #FFF;font-family: Prompt;font-size: 28px;font-style: normal;font-weight: 600;line-height: normal; margin-left: 70px;""")
        texte1.setContentsMargins(0, 100, 0, 0)
        texte1.setFixedSize(350, 30)
        #inputNomPropriete
        inputNomPropriete.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 10px;margin-left: 70px;""")
        inputNomPropriete.setFixedSize(550, 55)
        #adresseProp
        adresseProp.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        adresseProp.setFixedSize(550, 55)
        #coorEnregistrerProp
        coorEnregistrerProp.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        coorEnregistrerProp.setFixedSize(550, 55)
        #coorActuelProp
        coorActuelProp.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        coorActuelProp.setFixedSize(550, 55)
        #etatVoitureProp
        etatVoitureProp.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        etatVoitureProp.setFixedSize(550, 55)
        #infractionCirculaireVoiture
        infractionCirculaireVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        infractionCirculaireVoiture.setFixedSize(250, 55)
        #impotVoiture
        impotVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 5px;""")
        impotVoiture.setFixedSize(295, 55)
        #taxeVoiture
        taxeVoiture.setStyleSheet("""border-radius: 10px;border: 1px solid #575757;background: #2E3738;color: #898989;font-family: Prompt;
        font-size: 15px;font-style: normal;font-weight: 500;line-height: normal; padding-left : 20px;margin-left: 70px;""")
        taxeVoiture.setFixedSize(550, 55)


        #layout Page
        layoutPage = QHBoxLayout()
        #layout Menu
        layoutMenu = QVBoxLayout()
        layoutMenu.setContentsMargins(0, 0, 0, 80)

        layoutMenuTop = QHBoxLayout()
        layoutMenuTop.setContentsMargins(30, 10, 0, 0)
        layoutMenuTop.addWidget(Image)
        # layoutMenuTop.addWidget(propos)
        # layoutMenuTop.addWidget(Support)
        # layoutMenuTop.addWidget(Historique)
        # layoutMenuTop.addWidget(Parametre)
        # layoutMenuTop.addWidget(profil)


        layoutMenuBottom = QHBoxLayout()
        layoutMenuBottom.setContentsMargins(0, 0, 0, 0)
        layoutMenuBottomD = QVBoxLayout()
        layoutMenuBottomDI = QHBoxLayout()
        layoutMenuBottomD.addSpacing(-45)
        layoutMenuBottomD.addWidget(texte1)
        layoutMenuBottomD.addSpacing(40)
        layoutMenuBottomD.addWidget(inputNomPropriete)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(adresseProp)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomDI.addWidget(infractionCirculaireVoiture)
        layoutMenuBottomD.addLayout(layoutMenuBottomDI)
        layoutMenuBottomDI.addWidget(impotVoiture)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(coorEnregistrerProp)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(coorActuelProp)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(etatVoitureProp)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(taxeVoiture)
        layoutMenuBottomD.addSpacing(0)
        layoutMenuBottomD.addWidget(mandatCoursVoiture)
        layoutMenuBottomG = QVBoxLayout()
        layoutMenuBottomG.addWidget(mandatCoursVoiture)
        layoutMenuBottomG.addWidget(condamnationVoiture)
        layoutMenuBottomG.addWidget(activiteCrimVoiture)
        layoutMenuBottomG.addWidget(assuranceVoiture)
        layoutMenuBottomG.addWidget(dateAssuranceVoiture)
        layoutMenuBottomG.addWidget(dateAssurancePliceVoiture)
        layoutMenuBottomG.addWidget(accidentVoiture)
        layoutMenuBottomG.setContentsMargins(0, 0, 0, 0)

        layoutMenuBottom.addLayout(layoutMenuBottomD)
        layoutMenuBottom.addLayout(layoutMenuBottomG)


        layoutMenu.addLayout(layoutMenuTop)
        layoutMenu.addLayout(layoutMenuBottom)
        layoutPage.addLayout(layoutMenu)

        self.setLayout(layoutPage)
        self.setWindowTitle('Page3')
        self.setGeometry(200, 100, 1400, 450)
        self.setContentsMargins(0, 40, 100, 0)
        self.setStyleSheet("background: #05161F;")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    fenetre = MaFenetrePrincipale2()
    fenetre.show()
    sys.exit(app.exec_())


   
