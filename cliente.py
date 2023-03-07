class Cliente:

    def __init__(self, nome):
        self.__nome = nome
    #criando uma propriedade para poder chamar o nome()
    #title faz a 1ª letra do nome ficar maiúscula 
    #get
    @property
    def nome(self):
        return self.__nome.title()
    #set
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
