from abc import ABC, abstractmethod

class Vendedor(ABC):

    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__listaVendas = []

    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getCod(self):
        return self.__codigo
    
    def adicionaVenda(self,codImovel, mes, ano, valor):
        venda = Venda(codImovel, mes, ano, valor)
        self.__listaVendas.append(venda)

    @abstractmethod
    def getDados(self):
        pass

    @abstractmethod
    def calculaRenda(self):
        pass

class Venda():

    def __init__(self, codImovel, mes, ano, valor):
        self.__codImovel = codImovel
        self.__mes = mes
        self.__ano = ano
        self.__valor = valor

    @property
    def getCodImovel(self):
        return self.__codImovel

    @property
    def getMes(self):
        return self.__mes

    @property
    def getAno(self):
        return self.__ano

    @property
    def getValor(self):
        return self.__valor

class Contratado(Vendedor):

    def __init__(self, codigo, nome, salario, NroCartTrabalho):
        super().__init__(codigo, nome)
        self.__salario = salario
        self.__NroCartTrabalho = NroCartTrabalho

    @property
    def getNroCartTrabalho(self):
        return self.__NroCartTrabalho
    
    @property
    def getSalario(self):
         return self.__salario
    
    def getDados(self):
       return 'Nome: {} - Nro Carteira Trabalho: {}'.format(self.getNome, self.getNroCartTrabalho)

    def calculaRenda(self, mes, ano):
        renda = 0.0
        for venda in self._Vendedor__listaVendas:
            if venda.getMes == mes and venda.getAno == ano:
                renda = renda + (venda.getValor * 0.01)

        return renda + self.__salario
    
class Comissionado(Vendedor):

    def __init__(self, codigo, nome, nroCPF, comissao):
        super().__init__(codigo, nome)
        self.__nroCPF = nroCPF
        self.__comissao = comissao

    @property
    def getNroCPF(self):
        return self.__nroCPF
    
    @property
    def getComissao(self):
        return self.__comissao
    
    def getDados(self):
        return 'Nome: {} - Nro Carteira Trabalho: {}'.format(self.getNome, self.getNroCPF)

    def calculaRenda(self, mes, ano):
        renda = 0.0
        porcentagem = self.__comissao / 100
        for venda in self._Vendedor__listaVendas:
            if venda.getMes == mes and venda.getAno == ano:
                renda = renda + (venda.getValor * porcentagem)
        return renda
    
if __name__ == "__main__":

    funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    listaFunc = [funcContratado, funcComissionado]
    for func in listaFunc:
        print (func.getDados())
        print ("Renda no mês 3 de 2022: ")
        print (func.calculaRenda(3, 2022))