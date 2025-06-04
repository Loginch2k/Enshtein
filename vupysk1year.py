from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel,QRadioButton,QLineEdit


import json


def save_to_json():
    name = name_line.text()
    age = year_line.text()
    data = {
        "name": name,
        "age": age,
    }

    # Запис у файл
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(f"Словник записано в файл data.json")
    main_win.close()
    import vupysk1year2



app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Ознайомлення')

text1 = QLabel(main_win)
text1.setText('''Ця програма дозволяє вам за допомогою тесту Руф’є провести первинну діагностику вашого здоров’я.

Проба Руф’є являє собою навантажувальний комплекс, призначений для оцінки працездатності серця при фізичному навантаженні.
У стандартному варіанті частота пульсу за 15 секунд вимірюється тричі:

Після проведення 45 присідань за 45 секунд.
Після закінчення навантаження пульс підраховується знову: число пульсацій за перші 15 секунд, 30 секунд відпочинку, число пульсацій за останні 15 секунд.

''')
text1.move(50,0)
text1.resize(1000,200)

name = QLabel(main_win)
name.setText("Введіть ім'я:")
name.move(200,200)
name.resize(75,40)

year = QLabel(main_win)
year.setText("Введіть вік:")
year.move(200,250)
year.resize(75,40)

year_line = QLineEdit(main_win)
year_line.move(300,262)
year_line.resize(150,20)

name_line = QLineEdit(main_win)
name_line.move(300,212)
name_line.resize(150,20)

Buton_1window = QPushButton(main_win)
Buton_1window.setText("Почати")
Buton_1window.move(350,300)
Buton_1window.resize(230,70)
Buton_1window.clicked.connect(save_to_json)


main_win.show()
app.exec_()