import tkinter as tk
from tkinter import ACTIVE, messagebox
from tkinter import ttk
import os.path
import pickle

class ConsoleInvalido(Exception):
    pass

class GeneroInvalido(Exception):
    pass

class PrecoInvalido(Exception):
    pass

class Jogo():
    def __init__(self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__console = console
        self.__genero = genero
        self.__preco = preco
        self.__listaAvaliacoes = []

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def console(self):
        return self.__console
    
    @property
    def genero(self):
        return self.__genero

    @property
    def preco(self):
        return self.__preco
    
    def appendAvaliacao(self, nota):
        self.__listaAvaliacoes.append(nota)

    def media(self):
        if len(self.__listaAvaliacoes) == 0:
            return 0
        soma = 0
        for nota in self.__listaAvaliacoes:
            soma += int(nota)
        media = soma / len(self.__listaAvaliacoes)
        if media <= 1:
            media = 1
        elif media <=2:
            media = 2
        elif media <= 3:
            media = 3
        elif media <= 4:
            media = 4
        else:
            media = 5
        return media
    
class LimiteCadastraJogo(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Cadastro")

        self.frameCodigo = tk.Frame(self)
        self.frameTitulo = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameTitulo.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Código:")
        self.labelTitulo = tk.Label(self.frameTitulo, text="Título:")
        self.labelConsole = tk.Label(self.frameConsole, text="Console:")
        self.labelGenero = tk.Label(self.frameGenero, text="Genero:")
        self.labelPreco = tk.Label(self.framePreco, text="Preço:")
        self.labelCodigo.pack(side="left")
        self.labelTitulo.pack(side="left")
        self.labelConsole.pack(side="left")
        self.labelGenero.pack(side="left")
        self.labelPreco.pack(side="left")

        self.entryCodigo = tk.Entry(self.frameCodigo, width = 15) 
        self.entryTitulo = tk.Entry(self.frameTitulo, width = 15) 
        self.entryConsole = tk.Entry(self.frameConsole, width = 15) 
        self.entryGenero = tk.Entry(self.frameGenero, width = 15) 
        self.entryPreco = tk.Entry(self.framePreco, width = 15) 
        self.entryCodigo.pack(side="left")
        self.entryTitulo.pack(side="left")
        self.entryConsole.pack(side="left")
        self.entryGenero.pack(side="left")
        self.entryPreco.pack(side="left")

        self.enterButton = tk.Button(self.frameButton, text="Enter")
        self.clearButton = tk.Button(self.frameButton, text="Limpar")
        self.closeButton = tk.Button(self.frameButton, text="Fechar")
        self.enterButton.pack(side="left")
        self.clearButton.pack(side="left")
        self.closeButton.pack(side="left")
        self.enterButton.bind("<Button>", self.controle.cadastraHandler)
        self.clearButton.bind("<Button>", self.controle.limpaCadHandler)
        self.closeButton.bind("<Button>", self.controle.fechaCadHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteAvaliaJogo(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Avaliação")

        self.frameCodigo = tk.Frame(self)
        self.frameCombobox = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameCombobox.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text="Cod: ")
        self.labelCombobox = tk.Label(self.frameCombobox, text="Nota:")
        self.labelCodigo.pack(side="left")
        self.labelCombobox.pack(side="left")

        self.entryCodigo = tk.Entry(self.frameCodigo, width=15)
        self.entryCodigo.pack(side="left")

        self.notaCombobox = ttk.Combobox(self.frameCombobox, values=[1, 2, 3, 4, 5])
        self.notaCombobox.pack(side="left")

        self.buttonAtribui = tk.Button(self.frameButton, text="Atribuir")
        self.buttonFechar = tk.Button(self.frameButton, text="Fechar")
        self.buttonAtribui.pack(side="left")
        self.buttonFechar.pack(side="left")
        self.buttonAtribui.bind("<Button>", self.controle.atribuirHandler)
        self.buttonFechar.bind("<Button>", self.controle.fechaAvHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaJogo(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Consulta")

        self.frameCombobox = tk.Frame(self)
        #self.frameButton = tk.Button(self)
        self.frameCombobox.pack(side="left")
        #self.frameButton.pack(side="left")

        self.labelEstrelas = tk.Label(self.frameCombobox, text="Estrelas:")
        self.labelEstrelas.pack(side="left")
        self.combobox = ttk.Combobox(self.frameCombobox, values=[1, 2, 3, 4, 5])
        self.combobox.pack(side="left")
        self.combobox.bind("<<ComboboxSelected>>", controle.consultaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlJogo():
    def __init__(self):
        if not os.path.isfile("jogos.pickle"):
            self.listaJogos = []
        else:
            with open("jogos.pickle", "rb") as f:
                self.listaJogos = pickle.load(f)

    def cadastraJogo(self):
        self.limiteCad = LimiteCadastraJogo(self)

    def avaliaJogo(self):
        self.limiteAv = LimiteAvaliaJogo(self)

    def consultaJogo(self):
        self.limiteCon = LimiteConsultaJogo(self)

    def cadastraHandler(self, event):
        cont = 0
        codigo = self.limiteCad.entryCodigo.get()
        tit = self.limiteCad.entryTitulo.get()
        console = self.limiteCad.entryConsole.get()
        gen = self.limiteCad.entryGenero.get()
        preco = self.limiteCad.entryPreco.get()
        preco = float(preco)
        listaPermitida1 = ['Xbox', 'Playstation', 'Switch', 'PC']
        listaPermitida2 = ['Ação', 'Aventura', 'Estratégia', 'RPG', 'Esporte', 'Simulação']
        try:
            if console not in listaPermitida1:
                raise ConsoleInvalido()
            if gen not in listaPermitida2:
                raise GeneroInvalido()
            if preco < 0.0 or preco > 500.0:
                raise PrecoInvalido()
        except ConsoleInvalido:
            self.limiteCad.mostraJanela("Atenção", "Insira um console válido")
            cont = 1
        except GeneroInvalido:
            self.limiteCad.mostraJanela("Atenção", "Insira um gênero válido")
            cont = 1
        except PrecoInvalido:
            self.limiteCad.mostraJanela("Atenção", "Insira um preço válido")
            cont = 1
        print(cont)

        if cont == 0:
            jogo = Jogo(codigo, tit, console, gen, preco)
            self.listaJogos.append(jogo)
            self.limiteCad.mostraJanela("Sucesso", "Jogo Cadastrado")
            self.limpaCadHandler(event)
        else:
            self.limiteCad.mostraJanela("Atenção", "Jogo Não Cadastrado")

    def limpaCadHandler(self, event):
        self.limiteCad.entryCodigo.delete(0, tk.END)
        self.limiteCad.entryTitulo.delete(0, tk.END)
        self.limiteCad.entryConsole.delete(0, tk.END)
        self.limiteCad.entryGenero.delete(0, tk.END)
        self.limiteCad.entryPreco.delete(0, tk.END)
    
    def fechaCadHandler(self, event):
        self.limiteCad.destroy()

    def atribuirHandler(self, event):
        cod = self.limiteAv.entryCodigo.get()
        for jogo in self.listaJogos:
            if cod == jogo.codigo:
                nota = int(self.limiteAv.notaCombobox.get())
                jogo.appendAvaliacao(nota)
        self.limiteAv.mostraJanela("Sucesso", "Nota Atribuida")

    def fechaAvHandler(self, event):
        self.limiteAv.destroy()

    def consultaHandler(self, event):
        nota = int(self.limiteCon.combobox.get())
        res = ""
        for jogo in self.listaJogos:
            if jogo.media() == nota:
                res += "Jogo: " + jogo.titulo + " - Codigo: " + str(jogo.codigo) + "\n" \
                    + "Console: " + jogo.console  + "\n"  + "Preco: " + str(jogo.preco)
                res += "\n --------------- \n"

        self.limiteCon.mostraJanela('Resultados', res)

    def salvar(self):
         if len(self.listaJogos) != 0:
            with open("jogos.pickle","wb") as f:
                pickle.dump(self.listaJogos, f)