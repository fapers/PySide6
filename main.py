# ///////////////////////////////////////////
# 
# BY: SOUZA, F. P;
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
# Créditos ao autor: Wanderson do canal: 
# https://www.youtube.com/channel/UCy1fv5dh3wQEem1nFAUBJzw
# 
# Este projeto pode ser utilizado livremente para todos os fins, desde que
# mantenham os respectivos créditos apenas nos scripts Python, qualquer 
# informação na interface visual (GUI) pode ser modificada sem qualquer 
# implicação. 
# 
# Existem limitações nas licenças Qt se você quiser usar seus produtos 
# comercialmente, recomendo lê-las no site oficial: 
# https://doc.qt.io/qtforpython/licenses.html
# 
# ///////////////////////////////////////////

# IMPORT MODULES
import sys
import os

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.window.main_window.ui_main_window import UI_MainWindow

# CLASS MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # APP TITLE
        self.setWindowTitle("Curso de Python e PySide6")
        
        # SETUP MAIN WINDOW
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        
        # EXIBIR A APLICAÇÃO
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
