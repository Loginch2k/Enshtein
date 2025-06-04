from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel,QRadioButton,QLineEdit

import json


with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

P1 = int(data["P1"])
P2 = int(data["P2"])
P3 = int(data["P3"])
name = data['name']


result = 4 * (P1 + P2 + P3) - 200 / 10


main_win = QWidget()
main_win.setWindowTitle('Ознайомлення')
         


text1 = QLabel(main_win)
text1.setText(f'''
Ваш індекс Руф’є: {result}
ПрацеЗдатність серця: Вище середнього


''')
text1.move(150,150)
text1.resize(300,200)

name4 = QLabel(main_win)
name4.setText(name)
name4.move(150,190)
name4.resize(75,40)





main_win.show()
