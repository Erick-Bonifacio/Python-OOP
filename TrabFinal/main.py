import tkinter as tk
import cliente as cli
import produto as produto
from tkinter import messagebox
import random
from datetime import datetime

class Item():
  def __init__(self, produto, quantidade, date):
    self.__produto = produto
    self.__quant = quantidade
    self.__date = date

  @property
  def date(self):
    return self.__date

  @date.setter
  def date(self, value):
    self.__date = value

  @property
  def produto(self):
    return self.__produto

  def total(self):
    return self.__quant * self.__produto.preco

  @property 
  def quant(self):
    return self.__quant

  def __str__(self):
    return f'{self.__produto}'  + f' - Total: {self.total()}'

class NotaFiscal():
  def __init__(self, nroId, listaItens, data):
    self.__nroId = nroId
    self.__listaItens = listaItens
    self.__data = data

  @property
  def nroId(self):
    return self.__nroId

  @property
  def listaItens(self):
    return self.__listaItens

  @property
  def data(self):
    return self.__data

  def total(self):
      tot = 0.0
      for item in self.__listaItens:
        tot += item.total()
      return float(tot)

  def __str__(self):
    return f'Nro ID: {self.__nroId} - Total: {self.total()} \nData: {self.__data}'

class MainView():
  def __init__(self, root, controle):
    self.controle = controle
    self.root = root
    self.root.geometry('350x350')
    self.menubar = tk.Menu(self.root)        
    self.produtoMenu = tk.Menu(self.menubar)
    self.clienteMenu = tk.Menu(self.menubar)
    self.salvaMenu = tk.Menu(self.menubar)

    #Menu bar - Cliente:
    self.clienteMenu.add_command(label="Cadastrar cliente",
                                 command=self.controle.cadastraCliente)
    self.clienteMenu.add_command(label="Consultar cliente",
                                 command=self.controle.consultaCliente)
    self.clienteMenu.add_command(label="Faturamento por cliente", 
                                 command=self.controle.faturamentoCliente)
    self.clienteMenu.add_command(label="Vendas por cliente/período",
                                 command=self.controle.vendasCliente)

    #Menu bar - Produto:
    self.produtoMenu.add_command(label="Cadastrar produto",
                                 command=self.controle.cadastroProduto)
    self.produtoMenu.add_command(label="Consultar produto",
                                 command=self.controle.consultaProduto)
    self.produtoMenu.add_command(label="Faturamento por produto",
                                 command=self.controle.faturamentoProduto)
    self.produtoMenu.add_command(label="Faturamento por período",
                                 command=self.controle.faturamentoPeriodoProduto)

    self.menubar.add_cascade(label="Cliente", menu=self.clienteMenu)
    self.menubar.add_cascade(label="Produto", menu=self.produtoMenu)
    self.menubar.add_command(label="Salvar e fechar", command=self.controle.fecharProg)

    self.root.config(menu=self.menubar)

    self.frameFruFru = tk.Frame(self.root)
    self.frameFruFru.pack()
    self.frameCpf = tk.Frame(self.root)
    self.frameCpf.pack()
    self.frameNome = tk.Frame(self.root)
    self.frameNome.pack()
    self.frameCodigo = tk.Frame(self.root)
    self.frameCodigo.pack()
    self.frameQuantidade = tk.Frame(self.root)
    self.frameQuantidade.pack()
    self.frameData = tk.Frame()
    self.frameData.pack()
    self.frameListbox = tk.Frame(self.root)
    self.frameListbox.pack()
    self.frameButton = tk.Frame(self.root)
    self.frameButton.pack()

    self.labelFrufru = tk.Label(self.frameFruFru, text=" ")
    self.labelFrufru.pack(side="top")
    self.labelCpf = tk.Label(self.frameCpf, text="CPF: ")
    self.labelCpf.pack(side="left")
    self.inputCpf = tk.Entry(self.frameCpf, width=20)
    self.inputCpf.pack(side="left")
    self.buttonCpf = tk.Button(self.frameCpf, text="Ok", height=1)
    self.buttonCpf.pack(side="left")
    self.buttonCpf.bind("<Button>", self.controle.validaCpf)
    self.labelNome = tk.Label(self.frameNome, text="Nome do Cliente:   ")
    self.labelNome.pack(side="left")
    self.labelResult = tk.Label(self.frameNome,text="CPF inválido")
    self.labelResult.pack(side="left")
    self.labelData = tk.Label(self.frameData, text="Data (dd/mm/yyyy):")
    self.labelData.pack(side="left")
    self.inputData = tk.Entry(self.frameData, width=14)
    self.inputData.pack(side="left")
    self.labelCodigo = tk.Label(self.frameCodigo, text="Código: ")
    self.labelCodigo.pack(side="left")
    self.labelQuantidade = tk.Label(self.frameQuantidade, text="Quantidade:")
    self.labelQuantidade.pack(side="left")
    self.inputCodigo = tk.Entry(self.frameCodigo, width=23)
    self.inputCodigo.pack(side="left")
    self.inputQuantidade = tk.Entry(self.frameQuantidade, width=20)
    self.inputQuantidade.pack(side="left")

    self.listbox = tk.Listbox(self.frameListbox, width = 30, height = 10)
    self.listbox.pack(side="left")

    self.buttonLancar = tk.Button(self.frameButton, text="Lançar")
    self.buttonLancar.pack(side="left")
    self.buttonLancar.bind("<Button>", self.controle.lancar)
    self.buttonConcluir = tk.Button(self.frameButton, text="Concluir")
    self.buttonConcluir.pack(side="left")
    self.buttonConcluir.bind("<Button>", self.controle.concluir)
    self.buttonLimpar = tk.Button(self.frameButton, text='Limpar')
    self.buttonLimpar.pack(side="left")
    self.buttonLimpar.bind("<Button>", self.controle.limpar)
    self.buttonRemover = tk.Button(self.frameButton, text='Remover')
    self.buttonRemover.pack(side="left")
    self.buttonRemover.bind("<Button>", self.controle.remover)

  def addListbox(self, item):
    self.listbox.insert(tk.END, item)

  def removeListbox(self, item):
    self.listbox.delete(item)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class MainControl:

  def __init__(self):
    self.root = tk.Tk()

    self.ctrlCliente = cli.CtrlCliente(self)
    self.ctrlProduto = produto.CtrlProduto(self, self.ctrlCliente) 

    self.listaNotas = []
    self.listaItens = []

    self.view = MainView(self.root, self)

    self.root.title("Sistema de Vendas")

    self.root.mainloop()

  # Funções CallBack - Cliente
  def cadastraCliente(self):
    self.ctrlCliente.cadastraCliente()
  def consultaCliente(self):
    self.ctrlCliente.consultaCliente()
  def faturamentoCliente(self):
    self.ctrlCliente.faturamentoCliente()
  def vendasCliente(self):
    self.ctrlCliente.vendasCliente()

  # Funções CallBack - Produto 
  def cadastroProduto(self):
    self.ctrlProduto.cadastraProduto()
  def consultaProduto(self):
    self.ctrlProduto.consultaProduto()
  def faturamentoProduto(self):
    self.ctrlProduto.faturamentoProduto()
  def faturamentoPeriodoProduto(self):
    self.ctrlProduto.faturamentoPeriodoProduto()

  def validaCpf(self, event):
    cpf = self.view.inputCpf.get()
    for cliente in self.ctrlCliente.listaClientes:
      if str(cliente.cpf) == str(cpf):
        self.view.labelResult["text"]  = cliente.nome
        return

    self.view.labelResult.config(text="CPF inválido")
    self.view.mostraJanela("Erro", "CPF não cadastrado")
    self.cadastraCliente()

  def lancar(self, event):
    codigo = self.view.inputCodigo.get()
    quantidade = self.view.inputQuantidade.get()
    date_str = self.view.inputData.get().split('/')
    if len(self.listaItens) >= 10:
      self.view.mostraJanela("Atenção", "Limite de 10 produtos atingido")
    if len(date_str) != 3:
      self.view.mostraJanela("Atenção", "Preencha a data!")
      return
    if self.view.labelResult["text"] != "CPF inválido":
      if codigo == '' or quantidade == '':
        self.view.mostraJanela("Atenção", "Preencha os campos!")
        return
      for prod in self.ctrlProduto.listaProdutos:
        if prod.codigo == str(codigo):
          date = datetime(int(date_str[2]), int(date_str[1]), int(date_str[0]))
          print(date)
          item = Item(prod, float(quantidade), date)
          self.view.addListbox(item)
          self.listaItens.append(item)
          self.limpar(event)
          return
      self.view.mostraJanela("Atenção", "Nao existe produto com esse codigo!")
    else:
      self.view.mostraJanela("Atenção", "CPF inválido!")

  def limpar(self, event):
    self.view.inputCodigo.delete(0, tk.END)
    self.view.inputQuantidade.delete(0, tk.END)


  def concluir(self, event):
    if self.listaItens != [] and self.view.labelResult["text"] != "CPF inválido":
      id = random.randint(0, 1000000)
      date_str = self.view.inputData.get().split('/')
      if len(date_str) == 3:  
        date = datetime(int(date_str[2]), int(date_str[1]), int(date_str[0]))
        nota = NotaFiscal(id, self.listaItens, date)
        self.listaNotas.append(nota)
        for item in self.listaItens:
          for prod in self.ctrlProduto.listaProdutos:
            if prod.codigo == item.produto.codigo:
              item1 = item
              prod.appendItem(item1)
        self.listaItens =  []
        self.view.mostraJanela("Nota Fiscal", nota)
        for cliente in self.ctrlCliente.listaClientes:
          if str(cliente.cpf) == str(self.view.inputCpf.get()):
            cliente.adicionarCompra(nota)
        self.limpar(event)
        self.view.listbox.delete(0, tk.END)
        self.view.inputCpf.delete(0, tk.END)
        self.view.listbox.delete(0, tk.END)
        self.view.inputData.delete(0, tk.END)
        self.view.labelResult["text"] = "CPF inválido"

  def remover(self, event):
    self.view.listbox.delete(self.view.listbox.curselection())

  def fecharProg(self):
    self.ctrlCliente.salvaCliente()
    self.ctrlProduto.salvaProduto()
    self.root.destroy()

if __name__ == '__main__':
    c = MainControl()