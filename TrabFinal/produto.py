import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os.path
import pickle

class Produto():

  def __init__(self, codigo, descricao, preco):
    self.__codigo = codigo
    self.__descricao = descricao
    self.__preco = preco
    self.__listaVenda = []

  @property
  def codigo(self):
    return self.__codigo

  @property
  def descricao(self):
    return self.__descricao

  @property
  def preco(self):
    return self.__preco

  @property
  def listaVenda(self):
    return self.__listaVenda

  def appendItem(self, item):
    self.__listaVenda.append(item)

  def __str__(self):
    return f'{self.__codigo} - {self.__descricao}'


class CadastraView(tk.Toplevel):

  def __init__(self, controle):
    self.controle = controle

    tk.Toplevel.__init__(self)
    self.geometry('250x150')
    self.title("Cadastro")

    self.frameCodigo = tk.Frame(self)
    self.frameDescricao = tk.Frame(self)
    self.framePreco = tk.Frame(self)
    self.frameCodigo.pack()
    self.frameDescricao.pack()
    self.framePreco.pack()
    self.frameButton = tk.Frame(self)
    self.frameButton.pack()

    self.labelCodigo = tk.Label(self.frameCodigo, text="Código:")
    self.labelCodigo.pack(side="left")
    self.labelDescricao = tk.Label(self.frameDescricao, text="Descricao:")
    self.labelDescricao.pack(side="left")
    self.labelPreco = tk.Label(self.framePreco, text="Preco: ")
    self.labelPreco.pack(side="left")

    self.inputCodigo = tk.Entry(self.frameCodigo)
    self.inputCodigo.pack(side="left")
    self.inputDescricao = tk.Entry(self.frameDescricao)
    self.inputDescricao.pack(side="left")
    self.inputPreco = tk.Entry(self.framePreco)
    self.inputPreco.pack(side="left")

    self.buttonCadastrar = tk.Button(self.frameButton, text="Cadastrar")
    self.buttonCadastrar.pack(side="left")
    self.buttonCadastrar.bind("<Button>", controle.cadastrarProduto)
    self.buttonClear = tk.Button(self.frameButton, text="Limpar")
    self.buttonClear.pack(side="left")
    self.buttonClear.bind("<Button>", controle.limparCadHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class ConsultaView(tk.Toplevel):

  def __init__(self, controle):
    self.controle = controle

    tk.Toplevel.__init__(self)
    self.geometry('250x75')
    self.title("Consulta")

    self.frameCodigo = tk.Frame(self)
    self.frameCodigo.pack()
    self.frameButton = tk.Frame(self)
    self.frameButton.pack()

    self.labelCodigo = tk.Label(self.frameCodigo, text="Código:")
    self.labelCodigo.pack(side="left")
    self.inputCodigo = tk.Entry(self.frameCodigo)
    self.inputCodigo.pack(side="left")

    self.buttonConsultar = tk.Button(self.frameButton, text="Consultar")
    self.buttonConsultar.pack(side="left")
    self.buttonConsultar.bind("<Button>", controle.consultarProduto)
    self.buttonCancelar = tk.Button(self.frameButton, text="Limpar")
    self.buttonCancelar.pack(side="left")
    self.buttonCancelar.bind("<Button>", controle.limparConsHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class FaturamentoProdutoView(tk.Toplevel):

  def __init__(self, controle):
    self.controle = controle

    tk.Toplevel.__init__(self)
    self.geometry('250x75')
    self.title("Consulta de faturamento por produto")

    self.frameCodigo = tk.Frame(self)
    self.frameCodigo.pack()
    self.frameButton = tk.Frame(self)
    self.frameButton.pack()

    self.labelCodigo = tk.Label(self.frameCodigo, text="Código:")
    self.labelCodigo.pack(side="left")
    self.inputCodigo = tk.Entry(self.frameCodigo)
    self.inputCodigo.pack(side="left")

    self.buttonConsultar = tk.Button(self.frameButton, text="Consultar")
    self.buttonConsultar.pack(side="left")
    self.buttonConsultar.bind("<Button>", controle.faturamentoPorProduto)
    self.buttonCancelar = tk.Button(self.frameButton, text="Limpar")
    self.buttonCancelar.pack(side="left")
    self.buttonCancelar.bind("<Button>", controle.limparFatHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class FaturamentoPeriodoProdutoView(tk.Toplevel):

  def __init__(self, controle):
    self.controle = controle

    tk.Toplevel.__init__(self)
    self.geometry('250x75')
    self.title("Faturamento por período")
    self.controle = controle

    self.frameDataInicio = tk.Frame(self)
    self.frameDataFim = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameDataInicio.pack()
    self.frameDataFim.pack()
    self.frameButton.pack()

    self.labelDataInicio = tk.Label(self.frameDataInicio,
                                    text="Data de Inicio:")
    self.labelDataInicio.pack(side="left")
    self.inputDataInicio = tk.Entry(self.frameDataInicio, width=20)
    self.inputDataInicio.pack(side="left")

    self.labelDataFim = tk.Label(self.frameDataFim, text="Data de Fim:")
    self.labelDataFim.pack(side="left")
    self.inputDataFim = tk.Entry(self.frameDataFim, width=20)
    self.inputDataFim.pack(side="left")

    self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", controle.faturamentoPeriodoProd)

    self.buttonClear = tk.Button(self.frameButton, text="Clear")
    self.buttonClear.pack(side="left")
    self.buttonClear.bind("<Button>", controle.clearHandlerDatas)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)


class CtrlProduto():

  def __init__(self, controle, ctrlCliente):
    self.controle = controle
    self.ctrlCli = ctrlCliente
    #self.controladorPrincipal = MainControl :

    if not os.path.isfile("produtos.pickle"):
      self.listaProdutos = []
    else:
      with open("produtos.pickle", "rb") as f:
        self.listaProdutos = pickle.load(f)
    #self.listaProdutos = [Produto(101, "Patinho Bovino", 35.00)]

  def cadastraProduto(self):
    self.cadView = CadastraView(self)

  def consultaProduto(self):
    self.consView = ConsultaView(self)

  def faturamentoProduto(self):
    self.fatView = FaturamentoProdutoView(self)

  def faturamentoPeriodoProduto(self):
    self.fatProdView = FaturamentoPeriodoProdutoView(self)

  def cadastrarProduto(self, event):
    codigo = self.cadView.inputCodigo.get()
    descricao = self.cadView.inputDescricao.get()
    preco = self.cadView.inputPreco.get()
    if codigo == "" or descricao == "" or preco == "":
      self.cadView.mostraJanela("Erro", "Preencha todos os campos")
    else:
      preco = float(preco)
      if preco <= 0:
        self.cadView.mostraJanela("Erro", "Insira um prelo válido")
        return
      self.listaProdutos.append(Produto(codigo, descricao, preco))
      self.cadView.mostraJanela("Sucesso", "Produto cadastrado com sucesso")
      self.limparCadHandler(event)

  def limparCadHandler(self, event):
    self.cadView.inputCodigo.delete(0, tk.END)
    self.cadView.inputDescricao.delete(0, tk.END)
    self.cadView.inputPreco.delete(0, tk.END)

  def consultarProduto(self, event):
    codigo = self.consView.inputCodigo.get()
    if codigo == "":
      self.consView.mostraJanela("Erro", "Insira um código")
      return
    for prod in self.listaProdutos:
      if str(prod.codigo) == str(codigo):
        self.consView.mostraJanela(
            f"{prod.codigo}",
            f"Descrição:{prod.descricao}\nPreço: {prod.preco}")
        return
    self.consView.mostraJanela("Erro", "Produto não encontrado")

  def faturamentoPorProduto(self, event):
    codigo = self.fatView.inputCodigo.get()
    faturamento = 0.0
    cont = 0
    if codigo == "":
      self.fatView.mostraJanela("Erro", "Insira um código")
      return

    for prod in self.listaProdutos:
      if str(prod.codigo) == str(codigo):
        cont += 1
        for venda in prod.listaVenda:
          faturamento += float(venda.total())
    if (cont == 1):
      self.fatView.mostraJanela("Faturamento", f"Faturamento: {faturamento}")
    else:
      self.fatView.mostraJanela(
          "Erro", f"Não foi encontrado um produto com o código {codigo}")
    self.fatView.inputCodigo.delete(0, tk.END)

  def faturamentoPeriodoProd(self, event):
    dataIn = self.fatProdView.inputDataInicio.get()
    dataFim = self.fatProdView.inputDataFim.get()
    faturamento = 0
    cont = 0

    dataInicial = datetime.strptime(dataIn, "%d/%m/%Y")
    dataFinal = datetime.strptime(dataFim, "%d/%m/%Y")

    if dataIn == "" or dataFim == "":
      self.fatProdView.mostraJanela("Erro", "Insira uma data inicial e final")
      return

    for prod in self.listaProdutos:
      for item in prod.listaVenda:
        if item.date >= dataInicial and item.date <= dataFinal:
          faturamento += float(item.total())
          cont = 1

    if cont == 1:
      self.fatProdView.mostraJanela("Faturamento", f"R$ {faturamento}")
    else:
      self.fatProdView.mostraJanela("Erro",
                                    "Não foi encontrado vendas no período")
    self.fatProdView.inputDataFim.delete(0, tk.END)
    self.fatProdView.inputDataInicio.delete(0, tk.END)

  def limparFatHandler(self, event):
    self.fatView.inputCodigo.delete(0, tk.END)

  def limparConsHandler(self, event):
    self.consView.inputCodigo.delete(0, tk.END)

  def salvaProduto(self):
    if len(self.listaProdutos) != 0:
      with open("produtos.pickle", "wb") as f:
        pickle.dump(self.listaProdutos, f)

  def clearHandlerDatas(self, event):
    self.fatProdView.inputDataInicio.delete(0, tk.END)
    self.fatProdView.inputDataFim.delete(0, tk.END)
