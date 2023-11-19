import tkinter as tk
from tkinter import messagebox
import artista

class Musica():
    def __init__(self, titulo, nroFaixa):
        self.__titulo = titulo
        self.__nroFaixa = nroFaixa

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def nroFaixa(self):
        return self.__nroFaixa
    
    def __str__(self):
        return self.__titulo
    
class Album():
    def __init__(self, titulo, artista, ano, listaMusicas):
        self.__titulo = titulo
        self.__ano = ano
        self.__artista = artista
        self.__listaMusicas = listaMusicas

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def artista(self):
        return self.__artista
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def listaMusicas(self):
        return self.__listaMusicas
    
    def appendMusica(self, musica):
        self.__listaMusicas.append(musica)
    
class LimiteCadastraAlbum(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Musica")
        self.controle = controle

        self.frameTitulo = tk.Frame(self)
        self.frameArtista = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frameTitMusica = tk.Frame(self)
        self.frameNroFaixa = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameArtista.pack()
        self.frameAno.pack()
        self.frameTitMusica.pack()
        self.frameNroFaixa.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        self.labelTitulo = tk.Label(self.frameTitulo, text="Titulo:")
        self.labelArtista = tk.Label(self.frameArtista, text="Artista:")
        self.labelAno = tk.Label(self.frameAno, text="Ano:")
        self.labelTitMusica = tk.Label(self.frameTitMusica, text="Titulo da Musica:")
        self.labelNroFaixaMusica = tk.Label(self.frameNroFaixa, text="Nro da faixa")
        self.labelTitulo.pack(side="left")
        self.labelArtista.pack(side="left")
        self.labelAno.pack(side="left")
        self.labelTitMusica.pack(side="left")
        self.labelNroFaixaMusica.pack(side="left")

        self.tituloAlbumEntry = tk.Entry(self.frameTitulo, width = 15)
        self.artistaEntry = tk.Entry(self.frameArtista, width = 15)
        self.anoEntry = tk.Entry(self.frameAno, width = 15)
        self.tituloMusicaEntry = tk.Entry(self.frameTitMusica, width = 15)
        self.nroMusicaEntry = tk.Entry(self.frameNroFaixa, width = 15)
        self.tituloAlbumEntry.pack(side="left")
        self.artistaEntry.pack(side="left")
        self.anoEntry.pack(side="left")
        self.nroMusicaEntry.pack(side="left")
        self.tituloMusicaEntry.pack(side="left")

        self.insereMscButton = tk.Button(self.frameButton, text="Inserir Musica")
        self.cadastraAlbButton = tk.Button(self.frameButton, text="Cadastrar")
        self.consultarAlbButton = tk.Button(self.frameButton, text="Consultar")
        self.insereMscButton.pack(side = "left")
        self.cadastraAlbButton.pack(side = "left")
        self.insereMscButton.bind("<Button>", controle.insereMusica)
        self.cadastraAlbButton.bind("<Button>", controle.cadastraAlbum)
        self.clearButton = tk.Button(self.frameButton, text = "Limpar")
        self.clearButton.pack(side = "left")
        self.clearButton.bind("<Button>", controle.limpaCadHandler)

        self.closeButton = tk.Button(self.frameButton, text = "Fechar")
        self.closeButton.pack(side = "left")
        self.closeButton.bind("<Button>", controle.fechaCadHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaAlbum(tk.Toplevel):
    def __init__(self, controle):
        self.controle = controle

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta por Titulo")

        self.frameTitulo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameTitulo.pack()
        self.frameButton.pack()

        self.tituloLabel = tk.Label(self.frameTitulo, text="Titulo:")
        self.tituloLabel.pack(side="left")

        self.tituloEntry = tk.Entry(self.frameTitulo, width = 15)
        self.tituloEntry.pack(side="left")

        self.searchButton = tk.Button(self.frameButton, text="Pesquisar")
        self.searchButton.pack(side = "left")
        self.searchButton.bind("<Button>", controle.pesquisaHandler)

        self.clearButton = tk.Button(self.frameButton, text = "Limpar")
        self.clearButton.pack(side = "left")
        self.clearButton.bind("<Button>", controle.limpaConHandler)

        self.closeButton = tk.Button(self.frameButton, text = "Fechar")
        self.closeButton.pack(side = "left")
        self.closeButton.bind("<Button>", controle.fechaConHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlAlbum():
    def __init__(self, ctrlArt):
        self.listaAlbuns = []
        self.listaMusica = []
        self.controleArt = ctrlArt

    def CadastraAlbum(self):
        self.limiteCad = LimiteCadastraAlbum(self)

    def ConsultaAlbum(self):
        self.limiteCon = LimiteConsultaAlbum(self)

    def insereMusica(self, event):
        titulo = self.limiteCad.tituloMusicaEntry.get()
        nroFaixa = self.limiteCad.nroMusicaEntry.get()
        musica = Musica(titulo, nroFaixa)
        cont = 0
        for art in self.controleArt.listaArtista:
            if art.nome == self.limiteCad.artistaEntry.get():
                art.appendMusic(musica)
                cont += 1
        if cont == 0:
            self.limiteCad.mostraJanela("CUIDADO!", "Insira um artista valido!")
        else:
            self.listaMusica.append(musica)
            self.limiteCad.mostraJanela("Sucesso", "Musica salva!")
            self.limiteCad.tituloMusicaEntry.delete(0, len(self.limiteCad.tituloMusicaEntry.get()))
            self.limiteCad.nroMusicaEntry.delete(0, len(self.limiteCad.nroMusicaEntry.get()))
            

    def cadastraAlbum(self, event):
        nomeAlbum = self.limiteCad.tituloAlbumEntry.get()
        artista = self.limiteCad.artistaEntry.get()
        ano = self.limiteCad.anoEntry.get()
        album = Album(nomeAlbum, artista, ano, self.listaMusica)
        self.listaAlbuns.append(album)
        self.listaMusica = []
        self.limiteCad.mostraJanela("Sucesso", "Album cadastrado")
        self.limiteCad.destroy()
    
    def limpaCadHandler(self, event):
        self.limiteCad.tituloAlbumEntry.delete(0, len(self.limiteCad.tituloAlbumEntry.get()))
        self.limiteCad.tituloMusicaEntry.delete(0, len(self.limiteCad.tituloMusicaEntry.get()))
        self.limiteCad.nroMusicaEntry.delete(0, len(self.limiteCad.nroMusicaEntry.get()))
        self.limiteCad.tituloMusicaEntry.delete(0, len(self.limiteCad.tituloMusicaEntry.get()))
        self.limiteCad.anoEntry.delete(0, len(self.limiteCad.anoEntry.get()))
        self.limiteCad.artistaEntry.delete(0, len(self.limiteCad.artistaEntry.get()))
    
    def fechaCadHandler(self, event):
        self.limiteCad.destroy()
    
    def pesquisaHandler(self, event):
        str = ""
        titAlb = self.limiteCon.tituloEntry.get()
        for alb in self.listaAlbuns:
            if alb.titulo == titAlb:
                str = "Artista: " + alb.artista + " - Ano: " + alb.ano + "\n"
                for msc in alb.listaMusicas:
                    str += msc.titulo + " - " + msc.nroFaixa + "\n"

        self.limiteCon.mostraJanela("Album " + titAlb, str)

    def limpaConHandler(self, event):
        self.limiteCon.tituloEntry.delete(0, len(self.limiteCon.tituloEntry.get()))
    
    def fechaConHandler(self, event):
        self.limiteCon.destroy()