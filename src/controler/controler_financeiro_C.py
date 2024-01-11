from src.data_base.Operation_Crud_Financeiro_C import Operations_Crud_Financeiro_C
from src.data_base.Operations_Crud_Clientes import Operations_Crud_Clientes
from src.data_base.Operation_Crud_OS import Operations_Crud_OS
from src.data_base.Operation_Crud_Viagem import Operations_Crud_Viagem
from src.data_base.Operation_Crud_Estatisticas import Operations_Crud_Estatisticas
from src.data_base.Operation_Crud_Categorias import Operation_Crud_Categorias
from datetime import datetime

es = Operations_Crud_Estatisticas()
fn = Operations_Crud_Financeiro_C()
cl = Operations_Crud_Clientes()
os = Operations_Crud_OS()
vg = Operations_Crud_Viagem()
cat = Operation_Crud_Categorias()


def menu_financeiro_empresa():
    print('=-' * 30)

    menu = int(input('''
Financerio Empresa :
[1] Cadastrar Despesas   
[2] A Receber
[0] Voltar   
'''))
    print('=-' * 30)
    return menu


def start():
    while True:
        op = menu_financeiro_empresa()
        if op == 1:
            inserir_despesas()
        elif op == 2:
            a_receber()
        elif op == 0:
            break
        else:
            print('Opção Invalida')


def a_receber():
    while True:
        fn.search_a_receber('1', 'status', 'ABERTO')
        op = str(input('Fechar A Receber [S/N] ')).upper().strip()
        if op == 'S':
            id = int(input('ID '))
            fecha_a_receber(id)
            break
        elif op == 'N':
            break
        else:
            print('Opção Invalida')


def fecha_a_receber(a_receber_id, ):
    verifica = fn.a_receber_id_exists(a_receber_id)
    if verifica:
        op = str(input('Aleterar valor [S/N] ')).upper().strip()
        if op == 'S':
            valor = int(input('R$ '))
            fn.update_a_receber(a_receber_id, valor, 'FECHADO', '\n', a_receber_id)
            os.update('\n', '\n', '\n', valor, '\n', '\n',
                      '\n', '\n', a_receber_id, )
            cliente = os.search_db('1', 'cliente_id', a_receber_id)
            data = datetime.now().date()
            fn.insert_db_entrada(cliente, valor, data)
        else:
            fn.update_a_receber(a_receber_id, '\n', 'FECHADO', '\n', a_receber_id)
            cliente = os.search_db('1', 'cliente_id', a_receber_id)
            data = datetime.now().date()
            valor = os.search_db('1', 'valor', a_receber_id)
            fn.insert_db_entrada(cliente, valor, data)


# funçao sera usada no fechar mes para trazer a inserçao do valor abastecido:
def valor_abastecimento_empresa(mes):
    ano = datetime.today().date().year
    km_abastecimento = vg.get_abastecimento_km_by_month(ano, mes)
    valor_comb = vg.total_valor_abastecido(ano, mes)
    media_km_valor = km_abastecimento / valor_comb
    km_estatistica = es.total_km_rodado(ano, mes)
    result = media_km_valor * km_estatistica
    return result


def inserir_despesas():
    data = datetime.now().date()
    valor = int(input(('Valor ')))
    cat.search_categorias()
    c = str(input('Categoria '))
    categoria = cat.get_categoria_by_id(c)
    descricao = str(input('Descr. ')).upper()
    fn.insert_despesa_empresa(data, valor, categoria, descricao)



