from src.model import model_clientes
from src.model import model_financeiro

fn = model_financeiro
cl = model_clientes

def start():
    while True:

        op = cl.menu_geral()

        if op == 1:
            while True:
                op = cl.menu_cadastrar()
                if op == 1:
                    cl.cadastrar()
                elif op == 2:
                    cl.search()
                elif op == 3:
                    cl.update()
                elif op == 4:
                    cl.deletar()
                elif op == 0:
                    break
                else:
                    print('Opção Invalida')
        elif op == 2:
            while True:
                op = fn.menu_financeiro_geral()
                if op == 1:
                    fn.enter_insert()
                elif op == 2:
                    fn.saida_insert()
                elif op == 3:
                    fn.menu_relatorios_financiro()

                elif op == 0:
                    break
                else:
                    print('Opção Invalida')
        elif op == 3:
            # Logistica
            pass
        elif op == 0:
            break
        else:
            print('Opiçãp Invalida')
            #


if __name__ == "__main__":
    #sys.path.append(".")
    start()





