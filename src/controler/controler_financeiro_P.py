from src.data_base.Operation_Crud__Financeiro_P import Operations_Crud_Financeiro_P
from src.data_base.Operation_Crud_Categorias import Operation_Crud_Categorias
from src.data_base.Operation_Crud_Viagem import Operations_Crud_Viagem
from src.controler import controler_financeiro_C
from datetime import datetime

cat = Operation_Crud_Categorias()
vg = Operations_Crud_Viagem()
fn = Operations_Crud_Financeiro_P()
fnc = controler_financeiro_C


def menu_geral():
    menu = int(input("""
Finanças Pessoal
[1] Cadastrar Fixa
[2] Cadastrar Variavel
[3] Relatorios  
[0] Voltar 
"""))
    return menu

def menu_relatorio():
    menu = int(input("""
Relatorios
[1] Geral Fixa e Variaveis

"""))


def start():
    while True:
        op = menu_geral()
        if op == 1:
            insert_fixa()
        elif op == 2:
            insert_variavel()
        elif op == 0:
            break
        else:
            print('Opção Invalida')


# funçao sera usada no fechar mes para trazer a inserçao do valor abastecido:
def valor_abastecimento_pessoal(mes):
    ano = datetime.today().date().year
    valor_abast_empresa = fnc.valor_abastecimento_empresa(mes)
    valor_abast_total = vg.total_valor_abastecido(ano, mes)
    result = valor_abast_total - valor_abast_empresa
    return result


def insert_fixa():
    data = datetime.now().date()
    valor = float(input('Valor R$ '))
    cat.search_categorias()
    id_categoria = int(input('Digite a Categoria '))
    categoria = cat.get_categoria_by_id(id_categoria)
    descricao = str(input('Desc: '))
    fn.insert_despesa_fixa(data, valor, categoria, descricao)


def insert_variavel():
    data = datetime.now().date()
    valor = float(input('Valor R$ '))
    cat.search_categorias()
    id_categoria = int(input('Digite a Categoria '))
    categoria = cat.get_categoria_by_id(id_categoria)
    descricao = str(input('Desc: '))
    fn.insert_despesa_variavel(data, valor, categoria, descricao)



