from abc import ABC, abstractmethod

class TitulacaoInvalida(Exception):
    pass

class IdadeMenorQuePermitido(Exception):
    pass

class CursoInvalido(Exception):
    pass

class MenorDeIdade(Exception):
    pass

class CPFJaCadastrado(Exception):
    pass

class Pessoa(ABC):

    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf

    @property
    def getNome(self):
        return self.__nome
    
    @property
    def getEndereco(self):
        return self.__endereco
    
    @property
    def getIdade(self):
        return self.__idade
    
    @property
    def getCpf(self):
        return self.__cpf
    
    @abstractmethod
    def printDescricao(self):
        pass

class Professor(Pessoa):

    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao

    @property
    def getTitulacao(self):
        return self.__titulacao
    
    def printDescricao(self):
        print('Nome: {} - Idade: {}'.format(self.getNome, self.getIdade))
        print('endereco: {} - idd: {}'.format(self.getEndereco, self.getIdade))
        print('Titulacao: {}'.format(self.__titulacao))

class Aluno(Pessoa):

    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso

    @property
    def getCurso(self):
        return self.__curso
    
    def printDescricao(self):
        print('Nome: {} - Idade: {}'.format(self.getNome, self.getIdade))
        print('endereco: {} - idd: {}'.format(self.getEndereco, self.getIdade))
        print('Titulacao: {}'.format(self.__curso))

if __name__ == "__main__":

    listaPessoas = [Aluno('erick', 'Porto Amazonas',  18, 1234, 'SIN'),
                    Professor('Hokama', 'Av BPS', 35, 1235, 'Doutor'),
                    Aluno('Augusto', 'Osasco', 20, 1236, 'ECO'),
                    Aluno('erick', 'Moises Luize', 18, 1234, 'SIN'),
                    Aluno('DanDan', 'Moises Luize', 17, 1239, 'SIN'),
                    Professor('Bosco', 'Cel Renno', 70, 1237, 'Bacharel'),
                    Professor('Zezin', 'Logo Ali', 25, 1238, 'Doutor'),
                    Professor('Oto', 'pertin', 25, 1238, 'Doutor')      
    ]

    cadastro = {}

    for Pessoa in listaPessoas:
        if type(Pessoa) is Aluno:
            nome, endereco, idd, cpf, curso = Pessoa.getNome, Pessoa. getEndereco, Pessoa.getIdade, Pessoa.getCpf, Pessoa.getCurso
            try:
                if cpf in cadastro:
                    raise CPFJaCadastrado
                if idd < 18:
                    raise MenorDeIdade
                if curso != 'SIN' and curso != 'CCO':
                    raise CursoInvalido
            except CPFJaCadastrado:
                print('CPF de %s já cadastrado!' %nome)
            except MenorDeIdade:
                print('Aluno %s menor de idade!' %nome)
            except CursoInvalido:
                print('Curso %s Inválido!' %curso)
            else:
                cadastro[nome] = Aluno(nome, endereco, idd, cpf, curso)
        else:
            nome, endereco, idd, cpf, tit  = Pessoa.getNome, Pessoa.getEndereco, Pessoa.getIdade, Pessoa.getCpf, Pessoa.getTitulacao
            try:
                if idd < 30:
                    raise IdadeMenorQuePermitido
                if tit != 'Doutor' and tit != 'doutor':
                    raise TitulacaoInvalida
                if cpf in cadastro:
                    raise CPFJaCadastrado
            except IdadeMenorQuePermitido:
                print('Idade de %s menor que permitida' %nome)
            except TitulacaoInvalida:
                print('Tutulo de %s é inválido' %nome)
            except CPFJaCadastrado:
                print('CPF de %s já cadastrado anteriormente!' %nome)
            else:
                cadastro[nome] = Professor(nome, endereco, idd, cpf,  tit)

    print()
    
    for nome, pessoa in cadastro.items():
        print('Cadastro de', nome)
        pessoa.printDescricao()
        print()