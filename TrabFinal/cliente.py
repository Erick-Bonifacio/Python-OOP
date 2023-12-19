import tkinter as tk
from tkinter import messagebox
import pickle
from datetime import datetime
import os.path

class Cliente:
  def __init__(self, nome, endereco, email, cpf):
    self.__nome = nome
    self.__endereco = endereco
    self.__email = email
    self.__cpf = cpf
    self.__listaCompras = []

  @property
  def nome(self):
    return self.__nome

  @property
  def endereco(self):
    return self.__endereco

  @property
  def email(self):
    return self.__email

  @property
  def cpf(self):
    return self.__cpf

  def listaCompras(self):
    return self.__listaCompras

  def adicionarCompra(self, NF):
    self.__listaCompras.append(NF)

class CadastroClienteView(tk.Toplevel):
  def __init__(self, controle):

    tk.Toplevel.__init__(self)
    self.geometry('300x180')
    self.title("Cadastrar Cliente")
    self.controle = controle

    self.frameNome = tk.Frame(self)
    self.frameEndereco = tk.Frame(self)
    self.frameEmail = tk.Frame(self)
    self.frameCPF = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNome.pack()
    self.frameEndereco.pack()
    self.frameEmail.pack()
    self.frameCPF.pack()
    self.frameButton.pack()

    # Nome
    self.labelNome = tk.Label(self.frameNome,text="Nome do Cliente: ")
    self.labelNome.pack(side="left")  
    self.inputNome = tk.Entry(self.frameNome, width=20)
    self.inputNome.pack(side="left")      

    # Endereco
    self.labelEndereco = tk.Label(self.frameEndereco,text="Endereço do Cliente: ")
    self.labelEndereco.pack(side="left")  
    self.inputEndereco = tk.Entry(self.frameEndereco, width=20)
    self.inputEndereco.pack(side="left")   

    # Email
    self.labelEmail = tk.Label(self.frameEmail,text="Email do Cliente: ")
    self.labelEmail.pack(side="left")  
    self.inputEmail = tk.Entry(self.frameEmail, width=20)
    self.inputEmail.pack(side="left")

    # CPF
    self.labelCPF = tk.Label(self.frameCPF,text="CPF do Cliente: ")
    self.labelCPF.pack(side="left")  
    self.inputCPF = tk.Entry(self.frameCPF, width=20)
    self.inputCPF.pack(side="left")

    # Botões
    self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", controle.enterHandlerCad)

    self.buttonClear = tk.Button(self.frameButton ,text="Limpar")      
    self.buttonClear.pack(side="left")
    self.buttonClear.bind("<Button>", controle.clearHandlerCad)  

    self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
    self.buttonFecha.pack(side="left")
    self.buttonFecha.bind("<Button>", controle.closeHandlerCad)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class ConsultaClienteView(tk.Toplevel):
  def __init__(self, controle):

      tk.Toplevel.__init__(self)
      self.geometry('300x75')
      self.title("Consulta Cliente")
      self.controle = controle

      self.frameCPF = tk.Frame(self)
      self.frameButton = tk.Frame(self)
      self.frameCPF.pack()
      self.frameButton.pack()

      self.labelCPF = tk.Label(self.frameCPF,text="CPF do Cliente: ")
      self.labelCPF.pack(side="left")  

      self.inputCPF = tk.Entry(self.frameCPF, width=20)
      self.inputCPF.pack(side="left")             

      self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
      self.buttonSubmit.pack(side="left")
      self.buttonSubmit.bind("<Button>", controle.enterHandlerCon)

      self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
      self.buttonClear.pack(side="left")
      self.buttonClear.bind("<Button>", controle.clearHandlerCon)  

      self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
      self.buttonFecha.pack(side="left")
      self.buttonFecha.bind("<Button>", controle.closeHandlerCon)

  def mostraJanela(self, titulo, msg):
      messagebox.showinfo(titulo, msg)

class FaturamentoClienteView(tk.Toplevel):
  def __init__(self, controle):

      tk.Toplevel.__init__(self)
      self.geometry('300x75')
      self.title("Faturamento por Cliente")
      self.controle = controle

      self.frameCPF = tk.Frame(self)
      self.frameButton = tk.Frame(self)
      self.frameCPF.pack()
      self.frameButton.pack()

      self.labelCPF = tk.Label(self.frameCPF,text="CPF do Cliente: ")
      self.labelCPF.pack(side="left")  

      self.inputCPF = tk.Entry(self.frameCPF, width=20)
      self.inputCPF.pack(side="left")             

      self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
      self.buttonSubmit.pack(side="left")
      self.buttonSubmit.bind("<Button>", controle.faturamentoPorCliente)

      self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
      self.buttonClear.pack(side="left")
      self.buttonClear.bind("<Button>", controle.clearHandlerCon)  

      self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
      self.buttonFecha.pack(side="left")
      self.buttonFecha.bind("<Button>", controle.closeHandlerCon)

  def mostraJanela(self, titulo, msg):
      messagebox.showinfo(titulo, msg)

class VendasClientePeriodoView(tk.Toplevel):
  def __init__(self, controle):

    tk.Toplevel.__init__(self)
    self.geometry('300x130')
    self.title("Vendas por cliente/periodo")
    self.controle = controle

    self.frameCpf = tk.Frame(self)
    self.frameDataInicio = tk.Frame(self)
    self.frameDataFim = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameCpf.pack()
    self.frameDataInicio.pack()
    self.frameDataFim.pack()
    self.frameButton.pack()

    self.labelCPF = tk.Label(self.frameCpf,text="CPF:")
    self.labelCPF.pack(side="left")
    self.inputCPF = tk.Entry(self.frameCpf, width=20)
    self.inputCPF.pack(side="left")

    self.labelDataInicio = tk.Label(self.frameDataInicio,text="Data de Inicio:")
    self.labelDataInicio.pack(side="left")
    self.inputDataInicio = tk.Entry(self.frameDataInicio, width=20)
    self.inputDataInicio.pack(side="left")

    self.labelDataFim = tk.Label(self.frameDataFim,text="Data de Fim:")
    self.labelDataFim.pack(side="left")
    self.inputDataFim = tk.Entry(self.frameDataFim, width=20)
    self.inputDataFim.pack(side="left")

    self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")
    self.buttonSubmit.pack(side="left")
    self.buttonSubmit.bind("<Button>", controle.enterHandlerVendas)

    self.buttonClear = tk.Button(self.frameButton ,text="Clear")
    self.buttonClear.pack(side="left")
    self.buttonClear.bind("<Button>", controle.clearHandlerVendas)


  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class CtrlCliente():
  def __init__(self, controle):
    self.controle = controle
    if not os.path.isfile("clientes.pickle"):
      self.listaClientes = []
    else:
      with open("clientes.pickle", "rb") as f:
          self.listaClientes = pickle.load(f)
    #self.listaClientes.append(Cliente("João Silva Pereira", "Rua 1", "joao@gmail", 123))

  #cadastra
  def cadastraCliente(self):
    self.cadastraView = CadastroClienteView(self)

  def enterHandlerCad(self, event):
    nome = self.cadastraView.inputNome.get()
    endereco = self.cadastraView.inputEndereco.get()
    email = self.cadastraView.inputEmail.get()
    cpf = self.cadastraView.inputCPF.get()

    if len(nome) != 0:
      for cliente in self.listaClientes:
        if cliente.nome == nome:
          self.cadastraView.mostraJanela("Falha", "Cliente já cadastrado!")
          self.clearHandlerCad(event)
          return
      cliente = Cliente(nome, endereco, email, cpf)
      self.listaClientes.append(cliente)
      self.cadastraView.mostraJanela("Sucesso", "Cliente cadastrado!")
      self.clearHandlerCad(event)
    else:
      self.cadastraView.mostraJanela("Falha", "Digite algum nome!")
      self.clearHandlerCad(event)

  def clearHandlerCad(self, event):
    self.cadastraView.inputNome.delete(0,
            len(self.cadastraView.inputNome.get()))
    self.cadastraView.inputEndereco.delete(0, 
            len(self.cadastraView.inputEndereco.get()))
    self.cadastraView.inputEmail.delete(0,    
            len(self.cadastraView.inputEmail.get()))
    self.cadastraView.inputCPF.delete(0,
            len(self.cadastraView.inputCPF.get()))

  def closeHandlerCad(self, event):
    self.cadastraView.destroy()

  #consulta
  def consultaCliente(self):
    self.consultaClienteView = ConsultaClienteView(self)

  def enterHandlerCon(self, event):
    cpf = self.consultaClienteView.inputCPF.get()
    str1 = " "
    str2 = " "
    if len(cpf) != 0:
      for cliente in self.listaClientes:
        if str(cliente.cpf) == cpf:
          str1 = "Dados do CPF " + str(cliente.cpf)
          str2 = "\nNome: " + cliente.nome
          str2 += "\nEndereço: " + cliente.endereco 
          str2 += "\nEmail: " + cliente.email + "\n"

          self.consultaClienteView.mostraJanela(str1, str2)
          self.clearHandlerCon(event)
          return

      self.consultaClienteView.mostraJanela("Falha", "Cliente não cadastrado!")
      self.clearHandlerCon(event)
      self.cadastraCliente()  # CHAMA O CADASTRO  
    else:
        self.consultaClienteView.mostraJanela("Falha", "Insira um CPF!")


  def clearHandlerCon(self, event):
    self.consultaClienteView.inputCPF.delete(0, tk.END)

  def closeHandlerCon(self, event):
    self.consultaClienteView.destroy()

  #faturamento
  def faturamentoCliente(self):
    self.viewFat = FaturamentoClienteView(self)

  def faturamentoPorCliente(self, event):
    cpf = self.viewFat.inputCPF.get()
    faturamento = 0
    if len(cpf) != 0:
      for cliente in self.listaClientes:
        if str(cliente.cpf) == str(cpf):
          for compra in cliente.listaCompras():
            faturamento += compra.total()
          self.viewFat.mostraJanela(cliente.nome, "R$" + str(faturamento))
          return

      self.consultaClienteView.mostraJanela("Falha", "Cliente não cadastrado!")
      self.clearHandlerCon(event)


    else:
      self.consultaClienteView.mostraJanela("Falha", "Insira um CPF!")

  
  #Vendas
  def vendasCliente(self):
    self.vendasClienteView = VendasClientePeriodoView(self)

  def enterHandlerVendas(self, event):
    cpf = self.vendasClienteView.inputCPF.get()
    dataIn = self.vendasClienteView.inputDataInicio.get()
    dataFim = self.vendasClienteView.inputDataFim.get()
    faturamento = 0

    if len(cpf) != 0 and dataIn != '' and dataFim != '':
      try:
        dataInicio = datetime.strptime(dataIn, "%d/%m/%Y")
        dataFim = datetime.strptime(dataFim, "%d/%m/%Y")
      except ValueError:
        self.vendasClienteView.mostraJanela("Atenção", "Formato de data inválido!")
        return

      for cliente in self.listaClientes:
        if str(cliente.cpf) == str(cpf):
          for nf in cliente.listaCompras():
            if dataInicio <= nf.data <= dataFim:
                faturamento += nf.total()

          self.vendasClienteView.mostraJanela("Faturamento", f"R$ {faturamento}")
          return

      self.vendasClienteView.mostraJanela("Atenção", "Cliente não encontrado!")
    else:
        self.vendasClienteView.mostraJanela("Atenção", "Insira um CPF e datas válidas!")


  def clearHandlerVendas(self, event):
    self.vendasClienteView.inputCPF.delete(0,tk.END)
    self.vendasClienteView.inputDataInicio.delete(0, tk.END)
    self.vendasClienteView.inputDataFim.delete(0, tk.END)

  #salva
  def salvaCliente(self):
    if len(self.listaClientes) != 0:
      with open("clientes.pickle","wb") as f:
        pickle.dump(self.listaClientes, f)