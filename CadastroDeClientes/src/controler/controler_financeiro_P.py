from src.data_base.Operation_Crud_Operation_P import Operations_Crud_Financeiro_P
from src.data_base.Operation_Crud_Viagem import Operations_Crud_Viagem
from datetime import datetime
vg = Operations_Crud_Viagem()
fn = Operations_Crud_Financeiro_P()

def start_financerio_P():
    pass

def update_combustivel_variavel():
    ano = datetime.today().date().year
    mes = datetime.today().date().month
    km_abastecimento = vg.get_abastecimento_km_by_month(ano, mes)
    valor_comb = vg.get_media_valor_combustivel_mes(ano, mes)
    # aqui ele vai pegar o total de km_inicial - km_final da os, pelo ano/mes atual - km_abastecimento
    # fazer * autonomia * valor comb e adicionar a tabela variavel
