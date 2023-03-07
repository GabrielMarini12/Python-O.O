#criando uma classe
class Conta:
    #__init__ - criando uma função construtora
    #self é a referentecia que consegue encontrar o objeto que esta sendo construido
    #numero, titular, saldo, limite são atributos
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        # __ acesso sempre a partir dos metodos, atributos privados
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #criando metodo(função) extrato
    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
    #criando metodo(função) deposita
    def deposita(self, valor):
        self.__saldo += valor   

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar
    #criando metodo(função) saca
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))
    #criando metodo(função) transfere
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    #criando metodo(função) pega_saldo / get = não altera nada
    def get_saldo(self):
        return self.__saldo
    #criando metodo(função) devolve_titular
    def get_titular(self):
        return self.__titular
    #criando metodo(função) retorna_limite (get)
    @property
    def limite(self):
        return self.__limite
    #criando metodo(função) set_limite / set = altera
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    #criando metodo estatico, não precisa da classe nem criar objeto
    @staticmethod
    def codigo_banco():
        return "001"
