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

# IMPORT PAGES
from gui.pages.ui_pages import Ui_application_pages

# IMPORT CUSTOM WIDGETS
from gui.widgets.py_push_button import PyPushButton

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
        # self.main_layout = QVBoxLayout(self.central_frame)
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        # LEFT MENU ---------------------------------------------
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        # self.left_menu.setMaximumHeight(50)
        # self.left_menu.setMinimumHeight(50)
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        
        # LEFT MENU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)
        
        # TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        # self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: red; }")
        
        # TOP FRAME LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)
                
        # TOP BTN
        self.toggle_button = PyPushButton(
            text="Ocultar menu",
            icon_path="icon_menu.svg",
            icon_color="#c3ccdf"
        )
        self.btn_1 = PyPushButton(
            text="Página Inicial",
            is_active=True,
            icon_path="icon_home.svg"
        )
        self.btn_2 = PyPushButton(
            text="Página 2",
            icon_path="icon_widgets.svg"
        )
        self.btn_3 = PyPushButton(
            text="Página 3",
            icon_path="icon_home.svg"
        )
        
        # ADD BTN TO LAYOUT
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)
        # self.left_menu_top_layout.addWidget(self.btn_3)
        
        # MENU SPACER
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(40)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        # self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame { background-color: red; }")
        
        # BOTTOM FRAME LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)
        
        # BOTTOM BTN
        self.settings_btn = PyPushButton(
            text="Configurações",
            icon_path="icon_settings.svg"
        )
        
        # ADD BTN TO LAYOUT
        self.left_menu_bottom_layout.addWidget(self.settings_btn)
        
        # LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")
        
        # ADD TO LAYOUT
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        # ----------------------------------------- END LEFT MENU
        
        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")
        
        # # content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)
        
        # TOP BAR -------------------------------------
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)        
        
        # ## Left Label
        self.top_label_left = QLabel("Essa é minha primeira aplicação com PySide6")
        
        # ## Top spacer
        self.top_spacer = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # ## Right Label
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")
        
        # Add to Layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)
        # -------------------------------------FIM TOP BAR
        
        # ## APPLICATION PAGE
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_1)
        
        # BOTTOM BAR --------------------------------
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)        
        
        # ## Left Label
        self.bottom_label_left = QLabel("Criado por: Fábio P. Souza")
        
        # ## Top spacer
        self.bottom_spacer = QSpacerItem(20,20,QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        # ## Right Label
        self.bottom_label_right = QLabel("@ 2021")
        
        # Add to Layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)
        # ---------------------------------------FIM BOTTOM BAR       
        
        # ## Add to content Layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
                        
        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        # SET CENTRAL WIDGET
        parent.setCentralWidget(self.central_frame)
        