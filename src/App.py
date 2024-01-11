
from src.controler import controler_viagem, controler_clientes, controler_financeiro_geral, controler_os
fn = controler_financeiro_geral
cl = controler_clientes
lg = controler_viagem
os = controler_os

def start():
    while True:

        op = cl.menu_geral()

        if op == 1:
            cl.start_cliente()
        elif op == 2:
            fn.start()
        elif op == 3:
            lg.start_viagem()
        elif op == 4:
            os.start()
        elif op == 0:
            break
        else:
            print('Opiçãp Invalida')


if __name__ == "__main__":
    start()
