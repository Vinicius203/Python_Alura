class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo do titular {self.__titular} é: R$ {self.__saldo:.2f}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print(
                "O valor de saque é maior do que o saldo!"
                " A operação não foi realizada."
            )

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, limite):
        self.__limite = limite


conta = Conta(123, "Vinicius", 15.70, 1130)
conta2 = Conta(210, "Aragorn", 761.92, 3200)
