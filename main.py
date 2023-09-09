import sys
from PySide6.QtWidgets import (QApplication)
from PySide6.QtGui import (QIcon)
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import ButtonsGrid

if __name__ == '__main__':

    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o Icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText("Digite algo")
    window.addWidgetToVLayout(display)

    # Buttons
    # button = Button('Texto do botão')
    # window.addLayout(button)

    # button2 = Button('Texto do botão')
    # window.addLayout(button2)

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    window.ajustFixedSize()
    window.show()
    app.exec()
