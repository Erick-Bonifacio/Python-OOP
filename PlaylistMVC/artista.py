import tkinter as tk
from tkinter import messagebox

class Artista():
    def __init__(self, nome):
        self.__nome = nome
        self.__listaMusicas = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def listaMusicas(self):
        return self.__listaMusicas
    
    def appendMusic(self, music):
        self.__listaMusicas.append(music)

    def __str__(self):
        return self.nome
        
class LimiteCadastraArtista(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
        
        self.labelNome = tk.Label(self.frameNome, text="Nome:")
        self.labelNome.pack(side = "left")
        
        self.nameEntry = tk.Entry(self.frameNome, width = 20)
        self.nameEntry.pack(side = "left")

        self.submitButton = tk.Button(self.frameButton, text = "Submeter")
        self.submitButton.pack(side = "left")
        self.submitButton.bind("<Button>", controle.submeteHandler)

        self.clearButton = tk.Button(self.frameButton, text = "Limpar")
        self.clearButton.pack(side = "left")
        self.clearButton.bind("<Button>", controle.limpaCadHandler)

        self.closeButton = tk.Button(self.frameButton, text = "Fechar")
        self.closeButton.pack(side = "left")
        self.closeButton.bind("<Button>", controle.fechaCadHandler)
    
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaArtista(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consultar Artista")
        self.controle = controle

        self.nameFrame = tk.Frame(self)
        self.nameFrame.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        self.nameLabel = tk.Label(self.nameFrame, text = "Digite o nome:")
        self.nameLabel.pack(side = "left")

        self.nameEntry = tk.Entry(self.nameFrame, width = 20)
        self.nameEntry.pack(side = "left")

        self.searchButton = tk.Button(self.frameButton, text="Pesquisar")
        self.searchButton.pack(side="left")
        self.searchButton.bind("<Button>", controle.procuraHandler)

        self.clearButton = tk.Button(self.frameButton, text = "Limpar")
        self.clearButton.pack(side = "left")
        self.clearButton.bind("<Button>", controle.limpaConHandler)

        self.closeButton = tk.Button(self.frameButton, text = "Fechar")
        self.closeButton.pack(side = "left")
        self.closeButton.bind("<Button>", controle.fechaConHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlArtista():
    def __init__(self):
        self.listaArtista = [Artista("erick"), Artista("augusto")]
    
    def cadastraArtista(self):
        self.limiteCad = LimiteCadastraArtista(self)

    def consultaArtista(self):
        self.limiteCon = LimiteConsultaArtista(self)

    def submeteHandler(self, event):
        nome = self.limiteCad.nameEntry.get()
        artista = Artista(nome)
        self.listaArtista.append(artista)
        self.limiteCad.mostraJanela("Sucesso", "Cadastro Concluido!")
        self.limpaCadHandler(event)

    def limpaCadHandler(self, event):
        self.limiteCad.nameEntry.delete(0, len(self.limiteCad.nameEntry.get()))

    def fechaCadHandler(self, event):
        self.limiteCad.destroy()
    
    def limpaConHandler(self, event):
        self.limiteCon.nameEntry.delete(0, len(self.limiteCon.nameEntry.get()))

    def fechaConHandler(self, event):
        self.limiteCon.destroy()

    #def insereMusica(self, musica, event):
    #    self.appendMusic(musica)

    def procuraHandler(self, event):
        nome = self.limiteCon.nameEntry.get()
        str = "Artista: " + nome + "\n"
        for artista in self.listaArtista:
            if artista.nome == nome:
                for musica in artista.listaMusicas:
                    str += "Musica: " + musica.titulo + " - " + musica.nroFaixa + "\n"
                self.limiteCon.mostraJanela("Sucesso", str)