# import sys
# from PyQt5.QtWidgets import *
#
# app = QApplication(sys.argv)
# dlgMain = QDialog()
# dlgMain.setWindowTitle('First GUI')
# dlgMain.show()
#
# sys.exit(app.exec_())

from PyQt5.QtSql import QSqlDatabase
import settings as st
import sys
from PyQt5.QtWidgets import *
import psycopg2


class Application(QApplication):  # класс окна приложения
    def __init__(self, argv):
        super().__init__(argv)

        # db = QSqlDatabase.addDatabase('QPSQL')
        # db.setHostName(st.dp_params['host'])
        # db.setDatabaseName(st.dp_params['dbname'])
        # db.setPort(st.dp_params['port'])
        # db.setUserName(st.dp_params['user'])
        # db.setPassword(st.dp_params['password'])
        # ok = db.open()
        # if ok:
        #     print('Connected to database', file=sys.stderr)
        # else:
        #     print('Connection FAILED', file=sys.stderr)


class DlgRegistration(QDialog):  # класс окна регистрации
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
        conn = psycopg2.connect(dbname=st.dp_params['dbname'], user=st.dp_params['user'],
                                password=st.dp_params['password'], host=st.dp_params['host'])
        cursor = conn.cursor()
        try:
            cursor.execute(f"SELECT job FROM emploee WHERE password = '{str(self.ledText.text())}'")

            a = cursor.fetchone()[0]
            print(a)
            if 'директор' == a:
                dlgDirector.show()
                self.close()
            if 'администратор' == a:
                dlgAdmin.show()
                self.close()
            if 'бухгалтер' == a:
                dlgAccountant.show()
                self.close()
            if 'медсестра' == a:
                dlgNurse.show()
                self.close()
            if 'управляющий' == a:
                dlgManager.show()
                self.close()
        except:
            pass


class DlgDirector(QDialog):  # класс диалогового окна директора
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


class DlgAdmin(QDialog):  # класс диалогового окна администратора
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Администратор')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgAdmin.close()


class DlgAccountant(QDialog):  # класс диалогового окна бухгалтера
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Бухгалтер')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgAccountant.close()


class DlgNurse(QDialog):  # класс диалогового окна бухгалтера
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Медсестра')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgNurse.close()


class DlgManager(QDialog):  # класс диалогового окна бухгалтера
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Управляющий')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgManager.close()


if __name__ == '__main__':
    app = Application(sys.argv)

    dlgRegistration = DlgRegistration()
    dlgDirector = DlgDirector()
    dlgAdmin = DlgAdmin()
    dlgAccountant = DlgAccountant()
    dlgNurse = DlgNurse()
    dlgManager = DlgManager()
    dlgRegistration.show()

    sys.exit(app.exec_())
