import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase
import settings as st


class Application(QApplication):

    def __init__(self, argv):
        super().__init__(argv)

        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName(st.dp_params['host'])
        db.setDatabaseName(st.dp_params['dbname'])
        db.setPort(st.dp_params['port'])
        db.setUserName(st.dp_params['user'])
        db.setPassword(st.dp_params['password'])
        ok = db.open()
        if ok:
            print('Connected to database', file=sys.stderr)
        else:
            print('Connection FAILED', file=sys.stderr)
