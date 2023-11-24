import os.path
import pickle
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Curso():
    def __init__(self, sigla, nome):
        self.__sigla = sigla
        self.__nome = nome

    @property
    def sigla(self):
        return self.__sigla
    
    @property
    def nome(self):
        return self.__nome
    
class Estudante():
    def __init__(self, nroMatr, nome, curso):
        self.__nroMatr = nroMatr
        self.__nome = nome
        self.__curso = curso

    @property
    def nroMatr(self):
        return self.__nroMatr

    @property
    def nome(self):
        return self.__nome

    @property
    def curso(self):
        return self.__curso
    
class Equipe():
    def __init__(self, curso, estudantes):
        self.__curso = curso
        self.__listaEstudantes = estudantes

    @property
    def curso(self):
        return self.__curso

    @property
    def listaEstudantes(self):
        return self.__listaEstudantes

class LimiteCriaEquipe(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Cadastro")
        self.controle = controle

        self.frameCombobox = tk.Frame(self)
        self.frameEntry = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCombobox.pack()
        self.frameEntry.pack()
        self.frameButton.pack()

        self.labelCombobox = tk.Label(self.frameCombobox, text="Cursos:")
        self.labelCombobox.pack(side="left")

        self.labelEntry = tk.Label(self.frameEntry, text="NroMatr:")
        self.labelEntry.pack(side="left")

        listaCursos = [curso.nome for curso in controle.listaCurso]
        self.combobox = ttk.Combobox(self.frameCombobox, values=listaCursos)
        self.combobox.pack(side="left")
        
        self.nroMatrEntry = tk.Entry(self.frameEntry, width = 15)
        self.nroMatrEntry.pack()

        self.buttonConfirma = tk.Button(self.frameButton, text="Cria Equipe")
        self.buttonConfirma.pack(side="left")
        self.buttonConfirma.bind("<Button>", controle.confirmaCriaHandler)

        self.buttonInsereAluno = tk.Button(self.frameButton, text="Insere Aluno")
        self.buttonInsereAluno.pack(side="left")
        self.buttonInsereAluno.bind("<Button>", controle.insereHandler)
        
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaEquipe(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Consulta")
        self.controle = controle

        self.frameEntry = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameEntry.pack()
        self.frameButton.pack()

        self.labelEntry = tk.Label(self.frameEntry, text="Sigla:")
        self.labelEntry.pack(side="left")

        self.siglaEntry = tk.Entry(self.frameEntry, width=15)
        self.siglaEntry.pack(side="left")
        
        self.buttonPesquisa = tk.Button(self.frameButton, text="Pesquisar")
        self.buttonPesquisa.pack(side="left")
        self.buttonPesquisa.bind("<Button>", controle.pesquisaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteDados():       

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlEquipe():
    def __init__(self):
        c1 = Curso("CCO", "Ciência da Computação")
        c2 = Curso("SIN", "Sistemas de Informação")
        c3 = Curso("EEL", "Engenharia Elétrica")
        self.listaCurso = []
        self.listaCurso.append(c1)
        self.listaCurso.append(c2)
        self.listaCurso.append(c3)
        self.listaEstudante = []
        self.listaTemp = []
        self.listaEstudante.append(Estudante(1001, "José da Silva", c1))
        self.listaEstudante.append(Estudante(1002, "João de Souza", c1))
        self.listaEstudante.append(Estudante(1003, "Rui Santos", c2))
        self.listaEstudante.append(Estudante(1004, "Maria Clara", c2))
        self.listaEstudante.append(Estudante(1005, "Daniel Domingueti", c3))
        self.listaEstudante.append(Estudante(1006, "Augusto Juiz", c3))
        self.listaEstudante.append(Estudante(1007, "Amon Santos", c1))
        self.listaEstudante.append(Estudante(1008, "Pedro Nogueira", c2))
        self.listaEstudante.append(Estudante(1009, "Gabriel Barbosa", c3))
        self.listaEstudante.append(Estudante(1010, "Rafael Lima", c2))

        if not os.path.isfile("equipe.pickle"):
            self.listaEquipe = []
        else:
            with open("equipe.pickle", "rb") as f:
                self.listaEquipe = pickle.load(f)

    def criarEquipe(self):
        self.limiteCria = LimiteCriaEquipe(self)

    def consultaEquipe(self):
        self.limiteCons = LimiteConsultaEquipe(self)

    def imprimirDados(self):
        self.limiteDados = LimiteDados()
        totalEst = 0
        totalEq = len(self.listaEquipe)
        for equipe in self.listaEquipe:
            totalEst += len(equipe.listaEstudantes)
        media = totalEst/totalEq
        self.limiteDados.mostraJanela("OPA", "Total de equipes: " + str(totalEq) + "\nTotal de Estudantes: " + str(totalEst) + "\nMedia Estudante/Equipe: " + str(media))

    def salva(self):
        if len(self.listaEquipe) != 0:
            with open("equipe.pickle","wb") as f:
                pickle.dump(self.listaEquipe, f)
    
    def confirmaCriaHandler(self, event):
        nomeCurso = self.limiteCria.combobox.get()
        eq = Equipe(nomeCurso, self.listaTemp)
        self.listaTemp = []
        self.listaEquipe.append(eq)
        self.limiteCria.mostraJanela('Sucesso', 'Equipe criada!')
        self.limiteCria.destroy()

    def insereHandler(self, event):
        nroMat = self.limiteCria.nroMatrEntry.get()
        nome = self.limiteCria.combobox.get()
        cont = 0
        for estudante in self.listaEstudante:
            print('\n' + str(estudante.nroMatr) + '\n')
            print(str(nroMat) + '\n')
            print(estudante.curso.nome + '\n')
            print(self.limiteCria.combobox.get() + '\n')
            if str(estudante.nroMatr) == str(nroMat) and estudante.curso.nome == nome:
                cont = 1
                self.listaTemp.append(estudante)
                self.limiteCria.mostraJanela('Sucesso', "Estudante adicionado")
        if cont == 0:
            self.limiteCria.mostraJanela("Erro", "Estudante invalido")

    def pesquisaHandler(self, event):
        cont1 = 0
        cont2 = 0
        str = ''
        sigla = self.limiteCons.siglaEntry.get()
        for curso in self.listaCurso:
            if curso.sigla == sigla:
                cont1 = 1
                for equipe in self.listaEquipe:
                    if equipe.curso == curso.nome:
                        cont2 = 1
                        for estudante in equipe.listaEstudantes:
                            str += 'Aluno: ' + estudante.nome + '\n'

        if cont1 == 0:
            self.limiteCons.mostraJanela('Erro', 'Esta sigla nao existe')
        if cont2 == 0:
            self.limiteCons.mostraJanela('Erro', 'Nao existe equipe desse curso')

        if cont1 == 1 and cont2 == 1:
            self.limiteCons.mostraJanela('Resultado', str)
    