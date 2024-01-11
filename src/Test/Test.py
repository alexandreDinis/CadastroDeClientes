import tkinter as tk
from src.data_base.Operations_Crud_Clientes import Operations_Crud_Clientes


class App(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.operations_db = Operations_Crud_Clientes("clientes.db")

        self.create_widgets()

    def create_widgets(self):
        self.nome_label = tk.Label(self, text="Nome:")
        self.nome_entry = tk.Entry(self)

        self.contato_label = tk.Label(self, text="Contato:")
        self.contato_entry = tk.Entry(self)

        self.rua_label = tk.Label(self, text="Rua:")
        self.rua_entry = tk.Entry(self)

        self.bairro_label = tk.Label(self, text="Bairro:")
        self.bairro_entry = tk.Entry(self)

        self.cidade_label = tk.Label(self, text="Cidade:")
        self.cidade_entry = tk.Entry(self)

        self.phone_label = tk.Label(self, text="Telefone:")
        self.phone_entry = tk.Entry(self)

        self.setor_label = tk.Label(self, text="Setor:")
        self.setor_entry = tk.Entry(self)

        self.relevancia_label = tk.Label(self, text="Relevância:")
        self.relevancia_entry = tk.Entry(self)

        self.status_label = tk.Label(self, text="Status:")
        self.status_entry = tk.Entry(self)

        self.btn_inserir = tk.Button(self, text="Inserir", command=self.inserir)
        self.btn_atualizar = tk.Button(self, text="Atualizar", command=self.atualizar)
        self.btn_excluir = tk.Button(self, text="Excluir", command=self.excluir)

        self.nome_label.grid(row=0, column=1)
        self.nome_entry.grid(row=0, column=2)

        self.contato_label.grid(row=1, column=1)
        self.contato_entry.grid(row=1, column=2)

        self.rua_label.grid(row=2, column=1)
        self.rua_entry.grid(row=2, column=2)

        self.bairro_label.grid(row=3, column=1)
        self.bairro_entry.grid(row=3, column=2)

        self.cidade_label.grid(row=4, column=1)
        self.cidade_entry.grid(row=4, column=2)

        self.phone_label.grid(row=5, column=1)
        self.phone_entry.grid(row=5, column=2)

        self.setor_label.grid(row=6, column=1)
        self.setor_entry.grid(row=6, column=2)

        self.relevancia_label.grid(row=7, column=1)
        self.relevancia_entry.grid(row=7, column=2)

        self.status_label.grid(row=8, column=1)