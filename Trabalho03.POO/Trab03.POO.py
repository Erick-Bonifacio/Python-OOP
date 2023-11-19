from abc import ABC, abstractmethod

class EmpDomestica(ABC):

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
    
    @abstractmethod
    def getSalario(self):
        pass

class EmpHorista(EmpDomestica):

    def __init__(self, nome, telefone, horasTrabalhadas, salarioHora):
        super().__init__(nome, telefone)
        self.__horasTrabalhadas = horasTrabalhadas
        self.__salarioHora = salarioHora

    @property
    def _horasTrabalhadas(self):
        return self.__horasTrabalhadas

    @_horasTrabalhadas.setter
    def _horasTrabalhadas(self, value):
        self.__horasTrabalhadas = value

    @property
    def _salarioHora(self):
        return self.__salarioHora

    @_salarioHora.setter
    def _salarioHora(self, value):
        self.__salarioHora = value

    def getSalario(self):
        return self.__horasTrabalhadas * self.__salarioHora
    
class EmpDiarista(EmpDomestica):

    def __init__(self, nome, telefone, diasTrabalhados, salarioDia):
        super().__init__(nome, telefone)
        self.__diasTrabalhados = diasTrabalhados
        self.__salarioDia = salarioDia

    @property
    def _diasTrabalhados(self):
        return self.__diasTrabalhados

    @_diasTrabalhados.setter
    def _diasTrabalhados(self, value):
        self.__diasTrabalhados = value

    @property
    def _salarioDia(self):
        return self.__salarioDia

    @_salarioDia.setter
    def _salarioDia(self, value):
        self.__salarioDia = value

    def getSalario(self):
        return self.__diasTrabalhados * self.__salarioDia
    
class EmpMensalista(EmpDomestica):

    def __init__(self, nome, telefone, valorMensal):
        super().__init__(nome, telefone)
        self.__valorMensal = valorMensal

    @property
    def _valorMensal(self):
        return self.__valorMensal

    @_valorMensal.setter
    def _valorMensal(self, value):
        self.__valorMensal = value

    def getSalario(self):
        return self.__valorMensal
    
if __name__ == "__main__":

    empregada1 = EmpHorista('Solange', 35123456789, 160, 12)
    empregada2 = EmpDiarista('Simoni', 35123456780, 25, 65)
    empregada3 = EmpMensalista('Maria', 351234567891, 1200)

    print(empregada1.getSalario())
    print(empregada2.getSalario())
    print(empregada3.getSalario())
    print()

    menorPreco = empregada1.getSalario()
    melhorOpcao = empregada1

    if(empregada2.getSalario() < menorPreco):
        menorPreco = empregada2.getSalario()
        melhorOpcao = empregada2
        
    if(empregada3.getSalario() < menorPreco):
        menorPreco = empregada3.getSalario()
        melhorOpcao = empregada3

    print('A melhor opcao eh:')
    print('Nome: {}'.format(melhorOpcao.nome))
    print('telefone: {}'.format(melhorOpcao.telefone))
    print('Que recebe R${} por mes'.format(melhorOpcao.getSalario()))