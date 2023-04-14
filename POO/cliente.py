class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


cliente = Cliente('vinicius')
print(cliente.nome)

cliente.nome = 'marco'
print(cliente.nome)
