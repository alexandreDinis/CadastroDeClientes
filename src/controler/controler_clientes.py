import openpyxl
from datetime import datetime
from src.model.Clientes import Clientes
from src.data_base.Operations_Crud_Clientes import Operations_Crud_Clientes

clientes = Clientes
data_base = Operations_Crud_Clientes()


def menu_geral():
    print('=-' * 30)
    menu = int(input('''
Digite a Opção Desejada:
[1] Clientes 
[2] Financeiro 
[3] Logistica  
[4] O.S
[0] Finalizar   
'''))
    print('=-' * 30)

    return menu


def menu_cadastrar():
    print('=-' * 30)
    menu = int(input('''
Digite a Opção Desejada :
[1] Cadastrar   
[2] Relatorios 
[3] Atualizar
[4] Deletar   
[0] Voltar   
'''))
    print('=-' * 30)

    return menu


def menu_search():
    print('=-' * 30)
    menu = int(input('''
Digite a Opção Desejada :
[1] Relatorio personalizado  
[2] Relatorio Geral 
[0] Voltar
 '''))
    print('=-' * 30)

    return menu


def export_report_to_excel(results, filename):
    """
    Exporta um relatório para um documento do Excel.
    """
    # Cria um novo documento do Excel.
    workbook = openpyxl.Workbook()

    # Cria uma nova planilha.
    worksheet = workbook.active

    # Escreve o cabeçalho do relatório.
    worksheet.append \
        (['ID', 'Nome', 'Contato', 'Rua', 'Bairro', 'Cidade', 'Phone', 'Setor', 'Relevância', 'Status', 'Data'])

    # Escreve os resultados da pesquisa.
    for result in results:
        worksheet.append \
            ([result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8],
              result[9], result[10]])

    # Salva o documento.
    workbook.save(filename)

    return filename


def cadastrar():
    while True:
        print(f'{"Cadastro de Clientes".rjust(40)}')
        print('=-' * 30)
        nome = str(input('Nome Fantasia: ')).upper()
        contato = str(input('Contato: ')).upper()
        rua = str(input('Rua: ')).upper()
        bairro = str(input('Bairro: ')).upper()
        cidade = str(input('Cidade: ')).upper()
        phone = str(input('Phone: ')).upper()
        setor = str(input('Setor: ')).upper()
        while True:
            relevancia = buscador_relevancia()
            if relevancia is not None:
                break
        while True:
            status = buscador_staus()
            if status is not None:
                break
        data = datetime.now().date()
        clientes(nome, contato, rua, bairro, cidade, phone, setor, relevancia, status, data)
        data_base.insert_db(nome, contato, rua, bairro, cidade, phone, setor, relevancia, status, data)
        print('=-' * 30)

        op = str(input('Novo Cadastro [S/N]')).upper().strip()
        if op == 'N':
            break


def search():
    global opc, column, search
    while True:
        menu = menu_search()
        if menu == 1:
            opc = '1'
            p = int(input('''
Pesquise por: 
[1] ID
[2]Nome Fantasia
[3]Cidade
[4]Status
[5]Relevancia
[0]Voltar'''))

            if p == 1:
                column = 'id'
                search = str(input('Digite um ID ')).strip()
            elif p == 2:
                column = 'nome'
                search = str(input('Digite o Nome fantasia ')).strip().upper()
            elif p == 3:
                column = 'cidade'
                search = str(input('Digite a Cidade ')).strip().upper()
            elif p == 4:
                column = 'status'
                while True:
                    search = buscador_staus()
                    if search is not None:
                        break
            elif p == 5:
                column = 'relevancia'
                while True:
                    while True:
                        search = buscador_relevancia()
                        if search is not None:
                            break
            elif p == 0:
                break
            else:
                print('Opição Invalida')

            data_base.search_db(opc, column, search)

        elif menu == 2:
            opc = '-1'
            data_base.search_db(opc, '', '')
            m = str(input('Deseja Exportar o Arquivo para o Excel ? [S/N]')).upper().strip()
            if m in 'S':
                result = data_base.search_db('-1', '', '')
                file_name = 'relatorio.xlsx'
                # export_report_to_excel(result ,file_name)
        elif menu == 0:
            break
        else:
            print('Opição Invalida')


def deletar():
    while True:
        id = str(input('Digite o ID do cliente que deseja remover '))
        opc = '1'
        column = 'id'
        id = str(id)
        data_base.search_db(opc, column, id)
        t = str(input(f'Tem certeza que deseja deletar [S/N]')).upper().strip()
        if t == 'S':
            data_base.delete_db(id)
            break
        elif t == 'N':
            break
        else:
            print('Opção invalida')


def update():
    while True:
        print(f'{"Update de Clientes".rjust(40)}')
        print('=-' * 30)
        id = str(input('Digite o ID do cliente que deseja fazer o update '))
        opc = '1'
        column = 'id'
        id = str(id)
        data_base.search_db(opc, column, id)
        print('=-' * 30)
        print('Modifique os campos ou aparete enter\n')
        nome = str(input('Nome Fantasia: ')).upper()
        contato = str(input('Contato: ')).upper()
        rua = str(input('Rua: ')).upper()
        bairro = str(input('Bairro: ')).upper()
        cidade = str(input('Cidade: ')).upper()
        phone = str(input('Phone: ')).upper()
        setor = str(input('Setor: ')).upper()
        vc = str(input('Voce vai alterar a Relevancia ? [S/N]')).upper().strip()
        if vc == 'S':
            while True:
                relevancia = buscador_relevancia()
                if relevancia is not None:
                    break
        else:
            relevancia = '\n'
        vc = str(input('Voce vai alterar o Status ? [S/N]')).upper().strip()
        if vc == 'S':
            while True:
                status = buscador_staus()
                if status is not None:
                    break
        else:
            status = '\n'
        data_base.update(nome, contato, rua, bairro, cidade, phone, setor, relevancia, status, id)
        print('=-' * 30)

        op = int(input('Novo Update [1 = Sim | 0 = Nao ]'))

        if op == 0:
            break


def buscador_relevancia():
    id = str(input('Relevancia = [ 1 - FORTE | 2 -  MEDIO | 3 - FRACO ')).upper().strip()
    if id in '1,2,3':
        return data_base.buscar_valor_relevancia(id)
    else:
        return None


def buscador_staus():
    id = str(input('Status = [ 1 = ATIVO | 2 = INATIVO] | 3 = PROSPEC ')).upper().strip()
    if id in '1,2,3':
        return data_base.buscar_valor_status(id)
    else:
        return None


def start_cliente():
    while True:
        op = menu_cadastrar()
        if op == 1:
            cadastrar()
        elif op == 2:
            search()
        elif op == 3:
            update()
        elif op == 4:
            deletar()
        elif op == 0:
            break
        else:
            print('Opção Invalida')
