import urllib3
import csv
import unidecode

urllib3.disable_warnings()
from datetime import datetime
from modules.getDataBase import GetDataBase


print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Inicio da atividade'))

tb = GetDataBase()
ativos_tabelao = tb.tabelao()

arquivo = open('C:/Automations/checkAuditAccessAD/reportAD/ad-lista-user-ativos-cscalgar.csv', encoding="utf8")
linhas = csv.reader(arquivo)

list_linhas = []

for linha in linhas:
    list_linhas.append([linha[0].rstrip(),linha[1].rstrip()])

list_found = []
for list_active_csc in ativos_tabelao:
    for linha in list_linhas:
        if list_active_csc[0] == unidecode.unidecode(linha[1].upper()):
            list_found.append([unidecode.unidecode(linha[0].upper()), unidecode.unidecode(linha[1].upper())])

with open('C:/Automations/checkAuditAccessAD/reports/checkAuditAccessAD.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["USUARIO", "NOME"])

    for n in list_found:
        writer.writerow([unidecode.unidecode(n[0].upper()), unidecode.unidecode(n[1].upper())])

print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Fim da atividade'))