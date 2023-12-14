from PyQt5.QtWidgets import QTableView, QMessageBox, QDialog
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextEdit, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import pyqtSlot


class Model(QSqlQueryModel):

    def __init__(self, parent=None):
        super().__init__(parent)

        sql = '''
            select id_emploee, name, surname, lastname,
            birthdate, job, work experience, education,
            salary, phone_number from emploee;
        '''
        self.setQuery(sql)


class View(QTableView):

    def __init__(self, parent: None):
        super().__init__(parent)

        model = Model(parent=self)
        self.setModel(model)

        @pyqtSlot()
        def add(self):
            QMessageBox.information(self, 'Работник', 'Добавление')
            dia = Dialog(parent=self)
            dia.exec()

        @pyqtSlot()
        def update(self):
            QMessageBox.information(self, 'Работник', 'Редактирование')

        @pyqtSlot()
        def delete(self):
            QMessageBox.information(self,'Работник','Удаление')

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        fio_lbl = QLabel('Фамилия И.О.')
        self.__fio_edt = QLineEdit(parent=self)

        phone_lbl = QLabel('телефон', parent=self)
        self.__phone_edt = QLineEdit(parent=self)

        email_lbl = QLabel('e-mail', parent=self)
        self.__email_edt = QLineEdit(parent=self)

        ok_btn = QPushButton('OK', parent=self)
        cancel_btn = QPushButton('Отмена',parent=self)