from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLabel,QRadioButton,QLineEdit


main_win = QWidget()
main_win.setWindowTitle('Ознайомлення')


def save_to_json():

    main_win.close()
    import vupysk1year4


text1 = QLabel(main_win)
text1.setText("Виконайте 30 присідань за 45 секунд")
text1.move(250,150)
text1.resize(250,30)

Buton_1window = QPushButton(main_win)
Buton_1window.setText("Продовжити")
Buton_1window.move(250,300)
Buton_1window.resize(230,70)
Buton_1window.clicked.connect(save_to_json)


main_win.show()