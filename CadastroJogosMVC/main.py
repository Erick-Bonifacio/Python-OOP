import tkinter as tk
import jogo as jg

class LimitePrincipal():
    def __init__(self, root, controle):
        #renomeando o controlador
        self.controle = controle

        #iniciando a interface
        self.root = root
        self.root.geometry('200x75')

        #criando os menus
        self.menuBar = tk.Menu(self.root)
        self.menuJogo = tk.Menu(self.menuBar)
        self.menuSalvar = tk.Menu(self.menuBar)

        #adicionando "botoes" aos menus
        self.menuJogo.add_command(label="Cadastrar", command=self.controle.cadastraJogo)
        self.menuJogo.add_command(label="Consultar", command=self.controle.consultaJogo)
        self.menuJogo.add_command(label="Avaliar", command=self.controle.avaliaJogo)

        self.menuSalvar.add_command(label="Salvar", command=self.controle.salva)

        self.menuBar.add_cascade(label="Jogo", menu=self.menuJogo)
        self.menuBar.add_cascade(label="Salvar", menu=self.menuSalvar)

        #configura a barra de menu na janela (??)
        self.root.config(menu=self.menuBar)

class CtrlPrincipal():
    def __init__(self):
        #inicia o tk??
        self.root = tk.Tk()

        #chama a view principal
        self.limite = LimitePrincipal(self.root, self)

        #instancia os controladores auxiliares
        self.ctrlJogo = jg.CtrlJogo()

        #titulo da janela principal
        self.root.title("Bem Vindo!")

        # Inicia o mainloop
        self.root.mainloop()

    #chama as views auxiliares - callback do limite principal
    def cadastraJogo(self):
        self.ctrlJogo.cadastraJogo()
   
    def consultaJogo(self):
        self.ctrlJogo.consultaJogo()

    def avaliaJogo(self):
        self.ctrlJogo.avaliaJogo()

    def salva(self):
        self.ctrlJogo.salvar()

if __name__ == '__main__':
    c = CtrlPrincipal()