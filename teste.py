import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit
from PySide6.QtWidgets import QTextEdit, QPushButton, QGridLayout
from qt_material import apply_stylesheet


class MinhaTela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Automatização de Testes")
        self.setGeometry(100, 100, 400, 300)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Grid Layout
        grid_layout = QGridLayout()

        # Caixa de texto "Caixa Postal"
        label_caixa_postal = QLabel("Caixa Postal")
        grid_layout.addWidget(label_caixa_postal, 1, 1, 1, 1)

        self.caixa_postal = QLineEdit()
        grid_layout.addWidget(self.caixa_postal, 2, 1, 1, 1)

        # Botões Processar, Parâmetros e Resultado
        btn_processar = QPushButton("Processar")
        btn_parametros = QPushButton("Parâmetros")
        btn_resultado = QPushButton("Resultado")

        grid_layout.addWidget(btn_processar, 1, 2, 1, 1)
        grid_layout.addWidget(btn_parametros, 2, 2, 1, 1)
        grid_layout.addWidget(btn_resultado, 3, 2, 1, 1)

        # Caixa de texto para exibir o resultado do processamento
        self.caixa_resultado = QTextEdit()
        self.caixa_resultado.setPlaceholderText("Resultado do Processamento")
        grid_layout.addWidget(self.caixa_resultado, 4, 0, 1, 3)

        # Adicione o layout de grade ao layout vertical
        layout.addLayout(grid_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_amber.xml')  # Aplica o estilo Material
    tela = MinhaTela()
    tela.show()
    sys.exit(app.exec_())
