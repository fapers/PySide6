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
        
        # Toggle button
        self.ui.toggle_button.clicked.connect(self.toggle_button)
        
        # Btn home
        self.ui.btn_1.clicked.connect(self.show_page_1)
        
        # Btn widgets
        self.ui.btn_2.clicked.connect(self.show_page_2)
        
        # Btn settings
        self.ui.settings_btn.clicked.connect(self.show_page_3)
        
        # Change text
        self.ui.ui_pages.btn_change_text.clicked.connect(self.change_text)
        
        # EXIBIR A APLICAÇÃO
        self.show()
        
    def change_text(self):
        text = self.ui.ui_pages.lineEdit.text()
        new_text = "Olá, " + text
        self.ui.ui_pages.label_text.setText(new_text)
        
    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass
        
    def show_page_1(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_1)
        self.ui.btn_1.set_active(True)
        
    def show_page_2(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)
        
    def show_page_3(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_3)
        self.ui.settings_btn.set_active(True)
        
    def toggle_button(self):        
        # Get menu width
        menu_width = self.ui.left_menu.width()
        
        # Check with
        width = 50
        if menu_width == 50:
            width = 240
        
        # Start animation
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
