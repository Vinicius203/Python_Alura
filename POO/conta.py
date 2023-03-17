class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'O saldo de {self.titular} é: {self.saldo}!')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor

conta = Conta(123, 'Vinicius', 150.0, 1000)
conta.extrato()
conta.saca(15.0)
conta.extrato()
conta.deposita(65.0)
conta.extrato()
