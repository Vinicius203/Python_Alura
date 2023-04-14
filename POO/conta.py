class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O saldo de {self.__titular} é: {self.__saldo}!')

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou o limite!')

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}


conta = Conta(123, 'Vinicius', 150.0, 1000.0)
conta2 = Conta(321, 'Marco', 50.0, 100.0)

'''
print(conta.limite)
conta.limite = 2000.0
print('---- Alterando valor do limite ----')
print(conta.limite)
'''

print('---- Realizando saque ----')
conta.saca(1000)
conta.extrato()
conta.saca(1001)
conta.extrato()
print(Conta.codigo_banco())
codigos = Conta.codigos_bancos()
print(codigos['Caixa'])
