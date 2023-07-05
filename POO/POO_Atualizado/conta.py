class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f"O saldo do titular {self.titular} é: R$ {self.saldo:.2f}")

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print(
                "O valor de saque é maior do que o saldo!"
                " A operação não foi realizada."
            )


conta = Conta(123, "Vinicius", 15.70, 1130)
conta2 = Conta(210, "Aragorn", 761.92, 3200)

conta.extrato()
conta.deposita(4.30)
conta.extrato()
conta.saca(20.01)
conta.extrato()
