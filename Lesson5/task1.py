from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLabel, QVBoxLayout)
from random import randint

app = QApplication([])
mw=QWidget()
mw.setWindowTitle("Winner Identifier")
mw.move(100,100)
mw.resize(400,200)

button = QPushButton('Generate')
text = QLabel('Click to find out the winner')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
mw.setLayout(line)

def winn():
    number=randint(0,99)
    winner.setText(str(number))
    text.setText("Winner:")

button.clicked.connect(winn)

mw.show()
app.exec_()