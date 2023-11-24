import equipe as eq
import tkinter as tk

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle

        #iniciando a interface
        self.root = root
        self.root.geometry('200x75')

        self.menuBar = tk.Menu(self.root)
        self.menuEquipe = tk.Menu(self.menuBar)
        self.menuSalvar = tk.Menu(self.menuBar)
        
        self.menuEquipe.add_command(label="Cadastrar", command=self.controle.cadastraEquipe)
        self.menuEquipe.add_command(label="Consultar", command=self.controle.consultaEquipe)
        self.menuEquipe.add_command(label="Dados", command=self.controle.mostraDados)
        self.menuSalvar.add_cascade(label="Salvar", command=self.controle.salva)

        #self.menuSalvar.add_command(label="Salvar", command=self.controle.salva)

        self.menuBar.add_cascade(label="Equipe", menu=self.menuEquipe)
        self.menuBar.add_cascade(label="Salvar", menu=self.menuSalvar)

        #configura a barra de menu na janela (??)
        self.root.config(menu=self.menuBar)

class CtrlPrincipal():
    def __init__(self):
        self.root = tk.Tk()

        #chama a view principal
        self.limite = LimitePrincipal(self.root, self)

        #instancia os controladores auxiliares
        self.ctrlEquipe = eq.CtrlEquipe()

        #titulo da janela principal
        self.root.title("Bem Vindo!")

        # Inicia o mainloop
        self.root.mainloop()

    def cadastraEquipe(self):
        self.ctrlEquipe.criarEquipe()

    def consultaEquipe(self):
        self.ctrlEquipe.consultaEquipe()

    def mostraDados(self):
        self.ctrlEquipe.imprimirDados()

    def salva(self):
        self.ctrlEquipe.salva()

if __name__ == '__main__':
    c = CtrlPrincipal()