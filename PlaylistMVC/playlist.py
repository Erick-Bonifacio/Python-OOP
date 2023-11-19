import tkinter as tk
from tkinter import ACTIVE, messagebox
from tkinter import ttk


class Playlist():
    def __init__(self, nome):
        self.__nome = nome
        self.__listaMusicas = []


    @property
    def nome(self):
        return self.__nome
   
    @property
    def listaMusicas(self):
        return self.__listaMusicas
   
class LimiteCadastrarPlaylist(tk.Toplevel):
    def __init__(self, controle, ctrlArt):
        self.controle = controle
        self.ctrlArtista = ctrlArt
        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Playlist")


        self.frameNome = tk.Frame(self)
        self.frameComboBox = tk.Frame(self)
        self.frameListBox= tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameComboBox.pack()
        self.frameListBox.pack()
        self.frameButton.pack()


        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNome.pack(side="left")
        self.labelArtista = tk.Label(self.frameComboBox, text="Artistas:")
        self.labelArtista.pack(side="left")
        self.labelMusica = tk.Label(self.frameListBox, text="Musicas:")
        self.labelMusica.pack(side="left")


        self.nameEntry = tk.Entry(self.frameNome, width=15)
        self.nameEntry.pack(side="left")


        self.includeButton = tk.Button(self.frameButton, text="Incluir")
        self.cadastraButton = tk.Button(self.frameButton, text="Cadastrar")
        self.fecharButton = tk.Button(self.frameButton, text="Fechar")
        self.includeButton.pack(side="left")
        self.cadastraButton.pack(side="left")
        self.fecharButton.pack(side="left")
        self.includeButton.bind("<Button>", controle.incluiHandler)
        self.cadastraButton.bind("<Button>", controle.cadastrarHandler)
        self.fecharButton.bind("<Button>", controle.fechaCadHandler)


        self.listaArtistas = self.ctrlArtista.listaArtista
        self.listaMusicas = []


        self.artistCombobox = ttk.Combobox(self.frameComboBox, values=self.listaArtistas, width=15)
        self.artistCombobox.pack(side="left")
        self.artistCombobox.bind("<<ComboboxSelected>>", self.atualizaListaMusicas)
       
        self.musicList = tk.StringVar(value=self.listaMusicas)
        self.musicBox = tk.Listbox(self.frameListBox, listvariable=self.musicList, height=5)
        self.musicBox.pack(side="left")


    def atualizaListaMusicas(self, event):
        self.listaMusicas = []
        artEscolhido = self.artistCombobox.get()
        for art in self.listaArtistas:
            if str(art) == artEscolhido:  # Usando str(art) para comparar com o nome do artista escolhido
                for msc in art.listaMusicas:
                    self.listaMusicas.append(str(msc))  # Adicionando a representação em string da música
        self.musicList.set(self.listaMusicas)


    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class LimiteConsultaPlaylist(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta de Playlist")


        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()


        self.labelNome = tk.Label(self.frameNome, text="Nome:")
        self.labelNome.pack(side="left")


        self.nameEntry = tk.Entry(self.frameNome, width = 15)
        self.nameEntry.pack(side="left")


        self.searchButton = tk.Button(self.frameButton, text="Procurar")
        self.searchButton.pack(side="left")
        self.clearButton = tk.Button(self.frameButton, text="Limpar")
        self.clearButton.pack(side="left")
        self.fecharButton = tk.Button(self.frameButton, text="Fechar")
        self.fecharButton.pack(side="left")
        self.searchButton.bind("<Button>", controle.procuraHandler)
        self.clearButton.bind("<Button>", controle.limpaHandler)
        self.fecharButton.bind("<Button>", controle.fechaConHandler)


    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlPlay():
    def __init__(self, ctrlArt):
        self.controleArt = ctrlArt
        self.listaPlaylist = []
        self.listaMusicas = []


    def cadastraPlaylist(self):
        self.limiteCad = LimiteCadastrarPlaylist(self, self.controleArt)


    def consultaPlaylist(self):
        self.limiteCon = LimiteConsultaPlaylist(self)
   
    def incluiHandler(self, event):
        musica_selecionada = self.limiteCad.musicBox.get(ACTIVE)
        self.listaMusicas.append(musica_selecionada)
        indice_selecionado = self.limiteCad.musicBox.curselection()
        if indice_selecionado:
            self.limiteCad.musicBox.delete(indice_selecionado)
        self.limiteCad.mostraJanela("Sucesso", "Música adicionada!")


    def cadastrarHandler(self, event):
        nome = self.limiteCad.nameEntry.get()
        play = Playlist(nome)
        for msc in self.listaMusicas:
            play.listaMusicas.append(msc)
        self.listaMusicas = []
        self.listaPlaylist.append(play) 
        self.limiteCad.mostraJanela("Sucesso", "Playlist Cadastrada")
        self.fechaCadHandler(event)
   
    def fechaCadHandler(self, event):
        self.limiteCad.destroy()


    def procuraHandler(self, event):
        str = ""
        nome = self.limiteCon.nameEntry.get()
        print(nome + '\n')
        for play in self.listaPlaylist:
            print(play.nome + '\n')
            if play.nome == nome:
                print('fala tu2')
                str = "Musicas: \n"
                for msc in play.listaMusicas:
                    str += msc + "\n"
        self.limiteCon.mostraJanela(nome, str)
   
    def limpaHandler(self, event):
        self.limiteCon.nameEntry.delete(0, self.limiteCon.nameEntry.get())


    def fechaConHandler(self, event):
        self.limiteCon.destroy()

