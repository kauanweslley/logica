from PyQt5.QtWidgets import (QApplication, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QMessageBox)
from PyQt5.QtCore import pyqtSlot
from verificadordecpf24 import remover_caracter, validation_cpf

@pyqtSlot()
def verificarCPF():
    alerta = QMessageBox()
    cpf_digitado = cpf.text()
    a = validation_cpf(cpf_digitado)
    if a == True:
        alerta.setText("CPF digitado foi: " + cpf_digitado + " e ele é válido")
        alerta.exec_()
    else:
        alerta.setText("CPF digitado foi: " + cpf_digitado + " e ele é invalido")
        alerta.exec_()

app = QApplication([])
janela = QWidget()
layout = QVBoxLayout()

titulo = QLabel("Meu verificador de CPF")
layout.addWidget(titulo)
cpf = QLineEdit()
layout.addWidget(cpf)
botao1 = QPushButton("Verificador CPF")
botao1.clicked.connect(verificarCPF)
layout.addWidget(botao1)
janela.setLayout(layout)

janela.show()
app.exec_()