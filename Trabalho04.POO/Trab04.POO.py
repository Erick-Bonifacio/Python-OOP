
from abc import ABC, abstractmethod

class Transacao():
    def __init__(self, data, valor, descricao):
        self.__data = data
        self.__valor = valor
        self.__descricao = descricao
    
    def __str__(self):
        return f'Data: {self.__data}, Valor: {self.__valor}, Descrição: {self.__descricao}'

class Conta(ABC):
    def __init__(self, numeroConta, titular, saldo):
        self.__numeroConta = numeroConta
        self.__titular = titular
        self.__saldo = saldo
        
        self.__listaTransacao = []

    @property
    def numeroConta(self):
        return self.__numeroConta

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo
    
    def setSaldo(self, value):
        self.__saldo = value

    # igual para todos
    def deposito(self, value, data):
        if value < 0:
            return print('impossivel')
        self.__saldo = self.__saldo + value
        transacao = Transacao(data, value, 'Deposito')
        self.__listaTransacao.append(transacao)

    # usaremos sobrescrita de metodos
    def retirada(self, value, data):
        if value > self.__saldo:
            return print('impossivel')
        self.__saldo = self.__saldo - value
        transacao = Transacao(data, value, 'Retirada')
        self.__listaTransacao.append(transacao)

    # Diferente para todos
    @abstractmethod
    def imprimirExtrato(self):
        pass
    
class ContaPoup(Conta):

    def __init__(self, numeroConta, titular, saldo, aniversario):
        super().__init__(numeroConta, titular, saldo)
        self.__aniversario = aniversario

    @property
    def aniversario(self):
        return self.__aniversario
    
    def imprimirExtrato(self):
        print('NumConta: {}'.format(self.numeroConta))
        print('Titular: {}'.format(self.titular))
        print('Saldo: {}'.format(self.saldo))
        print('Aniversario: {}'.format(self.__aniversario))
        for transacao in self._Conta__listaTransacao:
            print(transacao)

class ContaComLimite(Conta):

    def __init__(self, numeroConta, titular, saldo, limite):
        super().__init__(numeroConta, titular, saldo)
        self.__limite = limite

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, value):
        self.__limite = value
    
    def retirada(self, value, data):
        if value > (self.saldo + self.__limite):
            print('impossivel')
        self.setSaldo((self.saldo - value))
        transacao = Transacao(data, value, 'Retirada')
        self._Conta__listaTransacao.append(transacao)
    
    def imprimirExtrato(self):
        print('NumConta: {}'.format(self.numeroConta))
        print('Titular: {}'.format(self.titular))
        print('Saldo: {}'.format(self.saldo))
        print('Limite: {}'.format(self.__limite))
        for transacao in self._Conta__listaTransacao:
            print(transacao)

class ContaComum(Conta):

    def __init__(self, numeroConta, titular, saldo):
        super().__init__(numeroConta, titular, saldo)

    def imprimirExtrato(self):
        print('NumConta: {}'.format(self.numeroConta))
        print('Titular: {}'.format(self.titular))
        print('Saldo: {}'.format(self.saldo))
        for transacao in self._Conta__listaTransacao:
            print(transacao)     

if __name__ == "__main__":

    conta1 = ContaComum(12345, 'Erick Bonifacio', 250)
    conta2 = ContaComLimite(12346, 'Pedro Lima', 1230, 1500)
    conta3 = ContaPoup(12347, 'Lucas Vieira', 2000, 15)

    conta1.deposito(1000, '28/09')
    print(conta1.saldo)
    conta1.retirada(500, '29/10')
    print(conta1.saldo)
    print()

    conta2.deposito(170, '28/09')
    print(conta2.saldo)
    conta2.retirada(2500, '29/09')
    print(conta2.saldo)
    print()

    conta3.deposito(2000, '28/09')
    print(conta3.saldo)
    conta3.retirada(750, '29/09')
    print(conta3.saldo)
    print()
    
    list = [conta1, conta2, conta3]

    for conta in list:
        conta.imprimirExtrato()
        print()