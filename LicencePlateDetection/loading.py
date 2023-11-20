import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget

class LoadingWindow(QMainWindow):
    def __init__(self):
        super(LoadingWindow, self).__init__()

        self.setWindowTitle("Chargement")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Ajouter une étiquette avec le GIF animé
        loading_label = QLabel(self)
        movie = QMovie("Balls.gif")
        loading_label.setMovie(movie)
        movie.start()

        # Ajouter un texte ou un autre contenu si nécessaire
        text_label = QLabel("Chargement en cours...", self)
        text_label.setAlignment(Qt.AlignCenter)

        # Ajouter les étiquettes au layout
        layout.addWidget(loading_label)
        layout.addWidget(text_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoadingWindow()
    window.show()
    sys.exit(app.exec_())
