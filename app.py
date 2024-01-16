import sys

from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow,
                               QPushButton, QWidget, QLabel, QVBoxLayout, QLineEdit, QToolButton)
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from design import botoes_design, label_design, duelistas


app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle('Duelo Milenar - Ranking Duelistas')

botao1 = QPushButton('EDITAR DUELISTAS')
botao1.setFixedSize(700, 80)
botao1.setStyleSheet(botoes_design)

botao2 = QPushButton('RANKING')
botao2.setFixedSize(500, 80)
botao2.setStyleSheet(botoes_design)

adicionar_duelista = QPushButton('Adicionar Duelista')
adicionar_duelista.setFixedSize(340, 50)
adicionar_duelista.setStyleSheet("font-size: 30px; background-color: gray; color: white;")

text_novo_duelista = QLineEdit()
text_novo_duelista.setFixedSize(335, 50)
text_novo_duelista.setStyleSheet("font-size: 30px; border: 2px solid black; padding: 5px")

layout = QGridLayout()

central_widget.setLayout(layout)

box_duelistas = QLabel()
box_duelistas.setStyleSheet("border-radius: 10px; background-color: white; border: 2px solid black;")

layout.addWidget(botao1, 1, 1, 1, 5)
layout.addWidget(botao2, 1, 6, 1, 3)
layout.addWidget(box_duelistas, 2, 1, 15, 5)
layout.addWidget(text_novo_duelista, 3, 1, 1, 3)
layout.addWidget(adicionar_duelista, 3, 2, 1, 4)

for n in range(0, len(duelistas)):
    label = QLabel(duelistas[n])
    label.setStyleSheet(label_design)
    label.setMaximumWidth(250)
    label.setMaximumHeight(50)
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label, n+5, 1, 1, 1)

    dim_pontos = QPushButton('-')
    dim_pontos.setStyleSheet("font-size: 40px; background-color: red;")
    dim_pontos.setFixedSize(50, 50)
    layout.addWidget(dim_pontos, n+5, 2, 1, 1)
    
    pontos = QLineEdit("0")
    pontos.setFixedSize(50, 50)
    pontos.setAlignment(Qt.AlignCenter)
    pontos.setStyleSheet("font-size: 20px;")
    layout.addWidget(pontos, n+5, 3, 1, 1)

    add_pontos = QPushButton('+')
    add_pontos.setStyleSheet("font-size: 40px; background-color: green;")
    add_pontos.setFixedSize(50, 50)
    layout.addWidget(add_pontos, n+5, 4, 1, 1)

    icon = QIcon("imagens/lixo.png")
    excluir = QPushButton()
    excluir.setIcon(icon)
    excluir.setStyleSheet("font-size: 30px;")
    excluir.setFixedSize(40, 50)
    layout.addWidget(excluir, n+5, 5, 1, 1)

# menuBar
menu = window.menuBar()

window.show()
app.exec()