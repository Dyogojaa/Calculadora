import sys
from PySide6.QtWidgets import (QApplication)
from PySide6.QtGui import (QIcon)
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button

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
    window.addToVLayout(info)

    # Display
    display = Display()
    # display.setPlaceholderText("Digite algo")
    window.addToVLayout(display)

    # Buttons
    button = Button('Texto do botão')
    window.addToVLayout(button)

    button2 = Button('Texto do botão')
    window.addToVLayout(button2)

    window.ajustFixedSize()
    window.show()
    app.exec()
