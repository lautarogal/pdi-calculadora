import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QUrl
from interfaz import * # Archivo generado por pyuic6
class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)





from PyQt6 import QtWidgets
from interfaz import Ui_Form 
class Calculadora(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Pantalla
        self.display = QtWidgets.QLineEdit(self)
        self.display.setGeometry(70, 0, 270, 30)
        self.display.setReadOnly(True)

        # Conectar botones
        self.ui.cero.clicked.connect(lambda: self.agregar("0"))
        self.ui.uno.clicked.connect(lambda: self.agregar("1"))
        self.ui.dos.clicked.connect(lambda: self.agregar("2"))
        self.ui.tres.clicked.connect(lambda: self.agregar("3"))
        self.ui.cuatro.clicked.connect(lambda: self.agregar("4"))
        self.ui.cinco.clicked.connect(lambda: self.agregar("5"))
        self.ui.seis.clicked.connect(lambda: self.agregar("6"))
        self.ui.siete.clicked.connect(lambda: self.agregar("7"))
        self.ui.ocho.clicked.connect(lambda: self.agregar("8"))
        self.ui.nueve.clicked.connect(lambda: self.agregar("9"))

        self.ui.suma.clicked.connect(lambda: self.agregar("+"))
        self.ui.resta.clicked.connect(lambda: self.agregar("-"))
        self.ui.multiplicacion.clicked.connect(lambda: self.agregar("*"))
        self.ui.division.clicked.connect(lambda: self.agregar("/"))
        self.ui.porcentaje.clicked.connect(lambda: self.agregar("%"))

        self.ui.coma.clicked.connect(lambda: self.agregar("."))

        self.ui.igual.clicked.connect(self.calcular)
        self.ui.ac.clicked.connect(self.limpiar)
        self.ui.borrar.clicked.connect(self.borrar)
        
    def agregar(self, texto):
        self.display.setText(self.display.text() + texto)

    def limpiar(self):
        self.display.clear()

    def borrar(self):
        self.display.setText(self.display.text()[:-1])

    def calcular(self):
        try:
            resultado = eval(self.display.text())
            self.display.setText(str(resultado))
        except:
            self.display.setText("Error")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())







if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
