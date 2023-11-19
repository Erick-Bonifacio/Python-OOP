import tkinter as tk
import artista as art
import playlist as play
import album as alb

class LimitePrincipal():
    def __init__(self, root, controle):
        #renomeando o controlador
        self.controle = controle

        #iniciando a interface
        self.root = root
        self.root.geometry('200x75')

        #criando os menus
        self.menuBar = tk.Menu(self.root)
        self.menuArtista = tk.Menu(self.menuBar)
        self.menuAlbum = tk.Menu(self.menuBar)
        self.menuPlaylist = tk.Menu(self.menuBar)
        
        #adicionando "botoes" aos menus
        self.menuArtista.add_command(label="Cadastrar", command=self.controle.cadastraArtista)
        self.menuArtista.add_command(label="Consultar", command=self.controle.consultaArtista)
        self.menuAlbum.add_command(label="Cadastrar", command=self.controle.cadastraAlbum)
        self.menuAlbum.add_command(label="Consultar", command=self.controle.consultaAlbum)
        self.menuPlaylist.add_command(label="Cadastrar", command=self.controle.cadastraPlaylist)
        self.menuPlaylist.add_command(label="Consultar", command=self.controle.consultaPlaylist)

        self.menuBar.add_cascade(label="Artista", menu=self.menuArtista)
        self.menuBar.add_cascade(label="Álbum", menu=self.menuAlbum)
        self.menuBar.add_cascade(label="Playlist", menu=self.menuPlaylist)

        #configura a barra de menu na janela (??)
        self.root.config(menu=self.menuBar)

class CtrlPrincipal():
    def __init__(self):
        #inicia o tk??
        self.root = tk.Tk()

        #chama a view principal
        self.limite = LimitePrincipal(self.root, self)

        #instancia os controladores auxiliares
        self.ctrlArt = art.CtrlArtista()
        self.ctrlAlb = alb.CtrlAlbum(self.ctrlArt)
        self.ctrlPlay = play.CtrlPlay(self.ctrlArt)

        #titulo da janela principal
        self.root.title("Bem Vindo!")

        # Inicia o mainloop
        self.root.mainloop()

    #chama as views auxiliares - callback do limite principal
    def cadastraArtista(self):
        self.ctrlArt.cadastraArtista()
    def consultaArtista(self):
        self.ctrlArt.consultaArtista()

    def cadastraAlbum(self):
        self.ctrlAlb.CadastraAlbum()
    def consultaAlbum(self):
        self.ctrlAlb.ConsultaAlbum()

    def cadastraPlaylist(self):
        self.ctrlPlay.cadastraPlaylist()
    def consultaPlaylist(self):
        self.ctrlPlay.consultaPlaylist()

if __name__ == '__main__':
    c = CtrlPrincipal()