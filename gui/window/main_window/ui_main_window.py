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

# IMPOST QT CORE
from qt_core import *

# MAIN WINDOW
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
        
        # SET INITIAL PARAMETERS
        parent.resize(1200,720)
        parent.setMinimumSize(960,540)
        
        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()
        # self.central_frame.setStyleSheet("background-color: #282a36")
        
        # CREATE MAIN LAYOUT
        self.main_layout = QVBoxLayout(self.central_frame)
        # self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        # LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumHeight(50)
        # self.left_menu.setMaximumWidth(50)
        
        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")
        
        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
        