from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel,QRadioButton,QLineEdit

import json



def save_to_json():
    
    P2 = name_line.text()
    P3 = year_line.text()
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    data['P2'] = P2
    data['P3'] = P3

    # Запис у файл
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Словник записано в файл data.json")
    main_win.close()
    import vupysk1year5

main_win = QWidget()
main_win.setWindowTitle('Ознайомлення')



text1 = QLabel(main_win)
text1.setText('''Протягом хвилини заміряйте пульс двічі:
за перші 15 секунд хвилини, потім за останні 15 секунд.
Результати запишіть у відповідні поля.

''')
text1.move(50,0)
text1.resize(1000,200)

name = QLabel(main_win)
name.setText("Результат:")
name.move(200,200)
name.resize(100,40)

year = QLabel(main_win)
year.setText("Результат після відпочинку:")
year.move(200,250)
year.resize(165,40)

year_line = QLineEdit(main_win)
year_line.move(380,262)
year_line.resize(150,20)

name_line = QLineEdit(main_win)
name_line.move(380,212)
name_line.resize(150,20)

Buton_1window = QPushButton(main_win)
Buton_1window.setText("Завершити")
Buton_1window.move(350,300)
Buton_1window.resize(230,70)
Buton_1window.clicked.connect(save_to_json)


main_win.show()