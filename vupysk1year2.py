from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel,QRadioButton,QLineEdit

import json


def save_to_json():
    P1 = result_line.text()
    
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    data['P1'] = P1
        

    
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Словник записано в файл data.json")
    main_win.close()
    import vupysk1year3


main_win = QWidget()
main_win.setWindowTitle('Ознайомлення')




text1 = QLabel(main_win)
text1.setText('''Виміряйте пульс за 15 секунд
Результат запишіть у відповідне поле''')
text1.move(250,150)
text1.resize(250,30)

result = QLabel(main_win)
result.setText("Введіть результат:")
result.move(80,300)
result.resize(150,40)

result_line = QLineEdit(main_win)
result_line.move(300,310)
result_line.resize(230,20)

Buton_1window = QPushButton(main_win)
Buton_1window.setText("Почати")
Buton_1window.move(300,500)
Buton_1window.resize(230,70)
Buton_1window.clicked.connect(save_to_json)

main_win.show()
