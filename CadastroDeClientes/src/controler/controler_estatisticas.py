from src.data_base.Operation_Crud_OS import Operations_Crud_OS
from src.data_base.Operation_Crud_Estatisticas import Operations_Crud_Estatisticas

est = Operations_Crud_Estatisticas()
os = Operations_Crud_OS()


def estatisticas(id_os, id_cliente, valor, km_ini, km_fin, hora_ini, hora_fin, data):
    km_rodado = km_fin - km_ini
    hora_trabalhada = hora_fin - hora_ini
    est.insert_estatistica(id_os, valor, id_cliente, 1, hora_trabalhada, km_rodado, data)

def estatisticas_detalhadas():
    pass

# ranking de cliente que mais comprou





