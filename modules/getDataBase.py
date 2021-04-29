import cx_Oracle
from settings.credentials import *
from settings.parameters import *
from settings.db import *

class GetDataBase():
    def __init__(self):
        pass

    def tabelao(self):
        # --------------------------- Abrindo conexão com Oracle ---------------------------
        conn = cx_Oracle.connect(user=CRD_USER_DB_FPW, password=CRD_PWD_DB_FPW, dsn=PAR_FPW_TNS)
        c = conn.cursor()

        # ----------------- fazendo select dos ativos nos tabelão -----------------
        c.execute(SELECT_ACTIVE_TABELAO)
        return c.fetchall()
        c.close()
