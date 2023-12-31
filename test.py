from PyQt5.QtSql import QSqlDatabase
import settings as st
import sys
from PyQt5.QtWidgets import *
import psycopg2


class Application(QApplication):  # класс окна приложения
    def __init__(self, argv):
        super().__init__(argv)


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


class DlgListOfVacationers(QDialog):  # класс окна списка проживающих
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список проживающих')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

        self.ledText = QLineEdit('Введите id удаляемого отдыхающего', self)
        self.ledText.move(250, 240)

        self.btnDelete = QPushButton('Удалить отдыхающего', self)
        self.btnDelete.move(250, 190)
        self.btnDelete.clicked.connect(self.evt_btn_delete_clicked)

    def evt_btn_back_clicked(self):
        dlgDirector.show()
        dlgListOfVacationers.close()

    def evt_btn_delete_clicked(self):
        conn = psycopg2.connect(dbname=st.dp_params['dbname'], user=st.dp_params['user'],
                                password=st.dp_params['password'], host=st.dp_params['host'])
        cursor = conn.cursor()


class DlgListOfVacationersN(QDialog):  # класс окна списка проживающих для медсестры
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список проживающих')
        self.resize(600, 600)

        self.ledText = QListWidget()

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgNurse.show()
        dlgListOfVacationersN.close()


class DlgListOfVacationersA(QDialog):  # класс окна списка проживающих для медсестры
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список проживающих')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgAccountant.show()
        dlgListOfVacationersA.close()


class DlgListOfVacationersAd(QDialog):  # класс окна списка проживающих для медсестры
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список проживающих')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgAdmin.show()
        dlgListOfVacationersAd.close()


class DlgListOfVacationersM(QDialog):  # класс окна списка проживающих для медсестры
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список проживающих')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgManager.show()
        dlgListOfVacationersM.close()


class DlgListOfGuests(QDialog):  # класс окна списка гостей
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список гостей')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgDirector.show()
        dlgListOfGuests.close()


class DlgListOfGuestsN(QDialog):  # класс окна списка гостей
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список гостей')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgNurse.show()
        dlgListOfGuestsN.close()


class DlgListOfGuestsAd(QDialog):  # класс окна списка гостей
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список гостей')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgAdmin.show()
        dlgListOfGuestsAd.close()


class DlgListOfGuestsA(QDialog):  # класс окна списка гостей
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список гостей')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgAccountant.show()
        dlgListOfGuestsA.close()


class DlgListOfGuestsAd(QDialog):  # класс окна списка гостей
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список гостей')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgAdmin.show()
        dlgListOfGuestsAd.close()


class DlgListOfGuestsM(QDialog):  # класс окна списка гостей
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список гостей')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgManager.show()
        dlgListOfGuestsM.close()


class DlgListOfWorkers(QDialog):  # класс окна списка сотрудников
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список сотрудников')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

        self.ledText = QListWidget()

        self.ledDeleteText = QLineEdit('Введите id удаляемого', self)
        self.ledDeleteText.move(250, 240)

        self.btnDelete = QPushButton('Удалить сотрудника', self)
        self.btnDelete.move(250, 190)
        self.btnDelete.clicked.connect(self.evt_btn_delete_clicked)

        self.btnAdd = QPushButton('Добавить сотрудника', self)
        self.btnAdd.move(250, 140)
        self.btnAdd.clicked.connect(self.evt_btn_add_clicked)

    def evt_btn_back_clicked(self):
        dlgDirector.show()
        dlgListOfWorkers.close()

    def evt_btn_delete_clicked(self):
        conn = psycopg2.connect(dbname=st.dp_params['dbname'], user=st.dp_params['user'],
                                password=st.dp_params['password'], host=st.dp_params['host'])
        cursor = conn.cursor()
        cursor.execute('CALL delete_emploee((%s))', (self.ledDeleteText.text(),))
        conn.commit()
        print(self.ledDeleteText.text())

    def evt_btn_add_clicked(self):
        dlgAddWorkerD.show()


class DlgListOfWorkersA(QDialog):  # класс окна списка сотрудников
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список сотрудников')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgAccountant.show()
        dlgListOfWorkersA.close()


class DlgAddWorkerD(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Добавление сотрудника')
        self.resize(1500, 1500)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(500, 1000)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

        self.btnAdd = QPushButton('Добавить', self)
        self.btnAdd.move(500, 1050)
        self.btnBack.clicked.connect(self.evt_btn_add_clicked)

        self.ledId = QLineEdit('Введите id', self)
        self.ledId.move(300, 1000)

        self.ledName = QLineEdit('Введите имя', self)
        self.ledName.move(300, 950)

        self.ledSurname = QLineEdit('Введите фамилия', self)
        self.ledSurname.move(300, 900)

        self.ledLastname = QLineEdit('Введите отчество', self)
        self.ledLastname.move(300, 850)

        self.ledBirthdate = QLineEdit('Введите дату рождения', self)
        self.ledBirthdate.move(300, 800)

        self.ledJob = QLineEdit('Введите должность', self)
        self.ledJob.move(300, 750)

        self.ledWorkExp = QLineEdit('Введите опыт работы', self)
        self.ledWorkExp.move(300, 700)

        self.ledEducation = QLineEdit('Введите образование', self)
        self.ledEducation.move(300, 650)

        self.ledSalary = QLineEdit('Введите зп', self)
        self.ledSalary.move(300, 600)

        self.ledPhone = QLineEdit('Введите номер телефона', self)
        self.ledPhone.move(300, 550)

        self.ledPassword = QLineEdit('Введите пароль', self)
        self.ledPassword.move(300, 500)

    def evt_btn_back_clicked(self):
        dlgListOfWorkers.show()
        dlgAddWorkerD.close()

    def evt_btn_add_clicked(self):
        conn = psycopg2.connect(dbname=st.dp_params['dbname'], user=st.dp_params['user'],
                                password=st.dp_params['password'], host=st.dp_params['host'])
        cursor = conn.cursor()
        cursor.execute('CALL add_emploee((%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s),(%s))',
                       (self.ledId.text(),
                        self.ledName.text(), self.ledSurname.text(),
                        self.ledLastname.text(), self.ledBirthdate.text(),
                        self.ledJob.text(),
                        self.ledWorkExp.text(), self.ledEducation.text(),
                        self.ledSalary.text(),
                        self.ledPhone.text(), self.ledPassword.text()))
        conn.commit()


class DlgListOfWorkersM(QDialog):  # класс окна списка сотрудников
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Список сотрудников')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

    def evt_btn_back_clicked(self):
        dlgManager.show()
        dlgListOfWorkersM.close()


class DlgDirector(QDialog):  # класс диалогового окна директора
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Директор')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

        self.btnListOfVacationers = QPushButton('Список проживающих', self)
        self.btnListOfVacationers.move(250, 240)
        self.btnListOfVacationers.clicked.connect(self.evt_btn_listofvacationers_clicked)

        self.btnListOfGuests = QPushButton('Список гостей', self)
        self.btnListOfGuests.move(250, 190)
        self.btnListOfGuests.clicked.connect(self.evt_btn_listofguests_clicked)

        self.btnListOfWorkers = QPushButton('Список сотрудников', self)
        self.btnListOfWorkers.move(250, 140)
        self.btnListOfWorkers.clicked.connect(self.evt_btn_listofworkers_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgDirector.close()

    def evt_btn_listofvacationers_clicked(self):
        dlgListOfVacationers.show()
        dlgDirector.close()

    def evt_btn_listofguests_clicked(self):
        dlgListOfGuests.show()
        dlgDirector.close()

    def evt_btn_listofworkers_clicked(self):
        conn = psycopg2.connect(dbname=st.dp_params['dbname'], user=st.dp_params['user'],
                                password=st.dp_params['password'], host=st.dp_params['host'])
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM emploee')
        workers = cursor.fetchall()
        dlgListOfWorkers.ledText.clear()
        for worker in workers:
            list_item = QListWidgetItem(str(worker))
            dlgListOfWorkers.ledText.addItem(list_item)

        dlgListOfWorkers.show()
        dlgListOfWorkers.ledText.show()
        dlgDirector.close()


class DlgAdmin(QDialog):  # класс диалогового окна администратора
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Администратор')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

        self.btnListOfVacationers = QPushButton('Список проживающих', self)
        self.btnListOfVacationers.move(250, 240)
        self.btnListOfVacationers.clicked.connect(self.evt_btn_listofvacationers_clicked)

        self.btnListOfGuests = QPushButton('Список гостей', self)
        self.btnListOfGuests.move(250, 190)
        self.btnListOfGuests.clicked.connect(self.evt_btn_listofguests_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgAdmin.close()

    def evt_btn_listofvacationers_clicked(self):
        dlgListOfVacationersAd.show()
        dlgAdmin.close()

    def evt_btn_listofguests_clicked(self):
        dlgListOfGuestsAd.show()
        dlgAdmin.close()


class DlgAccountant(QDialog):  # класс диалогового окна бухгалтера
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Бухгалтер')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

        self.btnListOfVacationers = QPushButton('Список проживающих', self)
        self.btnListOfVacationers.move(250, 240)
        self.btnListOfVacationers.clicked.connect(self.evt_btn_listofvacationers_clicked)

        self.btnListOfGuests = QPushButton('Список гостей', self)
        self.btnListOfGuests.move(250, 190)
        self.btnListOfGuests.clicked.connect(self.evt_btn_listofguests_clicked)

        self.btnListOfWorkers = QPushButton('Список сотрудников', self)
        self.btnListOfWorkers.move(250, 140)
        self.btnListOfWorkers.clicked.connect(self.evt_btn_listofworkers_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgAccountant.close()

    def evt_btn_listofvacationers_clicked(self):
        dlgListOfVacationersA.show()
        dlgAccountant.close()

    def evt_btn_listofguests_clicked(self):
        dlgListOfGuestsA.show()
        dlgAccountant.close()

    def evt_btn_listofworkers_clicked(self):
        dlgListOfWorkersA.show()
        dlgAccountant.close()


class DlgNurse(QDialog):  # класс диалогового окна медсестры
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Медсестра')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

        self.btnListOfVacationers = QPushButton('Список проживающих', self)
        self.btnListOfVacationers.move(250, 240)
        self.btnListOfVacationers.clicked.connect(self.evt_btn_listofvacationers_clicked)

        self.btnListOfGuests = QPushButton('Список гостей', self)
        self.btnListOfGuests.move(250, 190)
        self.btnListOfGuests.clicked.connect(self.evt_btn_listofguests_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgNurse.close()

    def evt_btn_listofvacationers_clicked(self):
        conn = psycopg2.connect(dbname=st.dp_params['dbname'], user=st.dp_params['user'],
                                password=st.dp_params['password'], host=st.dp_params['host'])
        cursor = conn.cursor()
        cursor.execute('SELECT vacationers_clubs()')
        vacationers = cursor.fetchall()
        dlgListOfVacationersN.ledText.clear()
        for vacationer in vacationers:
            list_item = QListWidgetItem(str(vacationer))
            dlgListOfVacationersN.ledText.addItem(list_item)

        dlgListOfVacationersN.ledText.show()
        dlgNurse.close()
    def evt_btn_listofguests_clicked(self):
        dlgListOfGuestsN.show()
        dlgNurse.close()


class DlgManager(QDialog):  # класс диалогового окна бухгалтера
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Управляющий')
        self.resize(600, 600)

        self.btnBack = QPushButton('Назад', self)
        self.btnBack.move(250, 290)
        self.btnBack.clicked.connect(self.evt_btn_back_clicked)

        self.btnListOfVacationers = QPushButton('Список проживающих', self)
        self.btnListOfVacationers.move(250, 240)
        self.btnListOfVacationers.clicked.connect(self.evt_btn_listofvacationers_clicked)

        self.btnListOfGuests = QPushButton('Список гостей', self)
        self.btnListOfGuests.move(250, 190)
        self.btnListOfGuests.clicked.connect(self.evt_btn_listofguests_clicked)

        self.btnListOfWorkers = QPushButton('Список сотрудников', self)
        self.btnListOfWorkers.move(250, 140)
        self.btnListOfWorkers.clicked.connect(self.evt_btn_listofworkers_clicked)

    def evt_btn_back_clicked(self):
        dlgRegistration.show()
        dlgManager.close()

    def evt_btn_listofvacationers_clicked(self):
        dlgListOfVacationersM.show()
        dlgManager.close()

    def evt_btn_listofguests_clicked(self):
        dlgListOfGuestsM.show()
        dlgManager.close()

    def evt_btn_listofworkers_clicked(self):
        dlgListOfWorkersM.show()
        dlgManager.close()


if __name__ == '__main__':
    app = Application(sys.argv)

    dlgRegistration = DlgRegistration()

    dlgListOfVacationers = DlgListOfVacationers()
    dlgListOfVacationersN = DlgListOfVacationersN()
    dlgListOfVacationersA = DlgListOfVacationersA()
    dlgListOfVacationersAd = DlgListOfVacationersAd()
    dlgListOfVacationersM = DlgListOfVacationersM()

    dlgListOfGuests = DlgListOfGuests()
    dlgListOfGuestsN = DlgListOfGuestsN()
    dlgListOfGuestsA = DlgListOfGuestsA()
    dlgListOfGuestsAd = DlgListOfGuestsAd()
    dlgListOfGuestsM = DlgListOfGuestsM()

    dlgListOfWorkers = DlgListOfWorkers()
    dlgListOfWorkersA = DlgListOfWorkersA()
    dlgListOfWorkersM = DlgListOfWorkersM()
    dlgAddWorkerD = DlgAddWorkerD()

    dlgDirector = DlgDirector()
    dlgAdmin = DlgAdmin()
    dlgAccountant = DlgAccountant()
    dlgNurse = DlgNurse()
    dlgManager = DlgManager()

    dlgRegistration.show()

    sys.exit(app.exec_())
