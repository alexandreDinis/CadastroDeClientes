from src.controler import controler_viagem, controler_clientes, controler_financeiro_C

fn = controler_financeiro_C
cl = controler_clientes
lg = controler_viagem


def start():
    while True:

        op = cl.menu_geral()

        if op == 1:
            cl.start_cliente()
        elif op == 2:
            while True:
                op = fn.menu_op_financeiro()
                if op == 1:
                    fn.start_financerio_C()
                elif op == 2:
                    pass
                elif op == 0:
                    break
                else:
                    print('Opção Invalida')
        elif op == 3:
            lg.start_viagem()
        elif op == 0:
            break
        else:
            print('Opiçãp Invalida')


if __name__ == "__main__":
    start()
