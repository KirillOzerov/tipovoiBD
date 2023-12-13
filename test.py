# import sys
# from PyQt5.QtWidgets import *
#
# app = QApplication(sys.argv)
# dlgMain = QDialog()
# dlgMain.setWindowTitle('First GUI')
# dlgMain.show()
#
# sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *


class DlgRegistration(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Регистрация')
        self.resize(600, 600)

        self.ledText = QLineEdit('Введите пароль', self)
        self.ledText.move(250, 250)

        self.btnRegistration = QPushButton('Далее', self)
        self.btnRegistration.move(250, 290)
        self.btnRegistration.clicked.connect(self.evt_btn_registration_clicked)

    def evt_btn_registration_clicked(self):
        dlgDirector.show()
        self.close()


class DlgDirector(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Директор')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgDirector.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    dlgRegistration = DlgRegistration()
    dlgDirector = DlgDirector()
    dlgRegistration.show()
    sys.exit(app.exec_())
