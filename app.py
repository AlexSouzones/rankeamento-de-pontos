# QMainWindow e centralWidget
# -> QApplication (app)
#   -> QMainWindow (window->setCentralWidget)
#       -> CentralWidget (central_widget)
#           -> Layout (layout)
#               -> Widget 1 (botao1)
#               -> Widget 2 (botao2)
#               -> Widget 3 (botao3)
#   -> show
# -> exec
import sys

from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget, QLabel, QVBoxLayout, QLineEdit, QToolButton)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtCore import Qt


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Duelo Milenar - Ranking Duelistas')

botoes_design = "font-size: 80px; background-color: transparent; background-image: url('imagens/button.png'); border-radius: 10;"
label_design = "font-size: 50px; background-color: gray; border-radius: 5; "

duelistas = ["Marcos", "Nelson", "Alexandre", "Alan", "Jefferson", "Gustavinho", "Francimark", "Lucas", "Ferbadi"]



botao1 = QPushButton('EDITAR DUELISTAS')
botao1.setFixedSize(700, 80)
botao1.setStyleSheet(botoes_design)

botao2 = QPushButton('RANKING')
botao2.setFixedSize(500, 80)
botao2.setStyleSheet(botoes_design)

adicionar_duelista = QPushButton('Adicionar')
adicionar_duelista.setFixedSize(200, 50)
adicionar_duelista.setStyleSheet("font-size: 30px;")

text_novo_duelista = QLineEdit()
text_novo_duelista.setFixedSize(250, 50)
text_novo_duelista.setStyleSheet("font-size: 30px; color: gray;")

layout = QGridLayout()

central_widget.setLayout(layout)

layout.addWidget(botao1, 1, 1, 1, 5)
layout.addWidget(botao2, 1, 6, 1, 3)
layout.addWidget(text_novo_duelista, 2, 1, 1, 3)
layout.addWidget(adicionar_duelista, 2, 2, 1, 3)


for n in range(0, len(duelistas)):
    label = QLabel(duelistas[n])
    label.setStyleSheet(label_design)
    label.setMaximumWidth(250)
    label.setMaximumHeight(50)
    layout.addWidget(label, n+3, 1, 1, 1)
    dim_pontos = QPushButton('-')
    dim_pontos.setStyleSheet("font-size: 40px; background-color: red;")
    dim_pontos.setFixedSize(50, 50)
    layout.addWidget(dim_pontos, n+3, 2, 1, 1)
    
    pontos = QLineEdit("0")
    pontos.setFixedSize(50, 50)
    pontos.setAlignment(Qt.AlignCenter)
    pontos.setStyleSheet("font-size: 20px;")
    layout.addWidget(pontos, n+3, 3, 1, 1)

    add_pontos = QPushButton('+')
    add_pontos.setStyleSheet("font-size: 40px; background-color: green;")
    add_pontos.setFixedSize(50, 50)
    layout.addWidget(add_pontos, n+3, 4, 1, 1)

    icon = QIcon("imagens/lixo.png")
    excluir = QPushButton()
    excluir.setIcon(icon)
    excluir.setStyleSheet("font-size: 30px;")
    excluir.setFixedSize(40, 50)
    layout.addWidget(excluir, n+3, 5, 1, 1)
    
def slot_example(status_bar):
    status_bar.showMessage('O meu slot foi executado')


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('...')

# menuBar
menu = window.menuBar()
primeiro_menu = menu.addMenu('Menu')
primeira_acao = primeiro_menu.addAction('Primeira ação')
primeira_acao.triggered.connect(  # type:ignore
    lambda: slot_example(status_bar)
)


window.show()
app.exec()  # O loop da aplicação