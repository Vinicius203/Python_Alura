class Conta:
    def __init__(self, numero, titular, saldo, limite, codigo_banco):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"O saldo do titular {self.__titular} é: R$ {self.__saldo:.2f}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        if self.__possibilidade_saque(valor):
            self.__saldo -= valor
        else:
            print(
                "O valor de saque é maior do que o limite!"
                " A operação não foi realizada."
            )

    def __possibilidade_saque(self, valor_saque):
        valor_maximo = self.__saldo + self.__limite
        return valor_saque <= valor_maximo

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


print(Conta.codigo_banco())
print(Conta.codigos_bancos())

conta = Conta(123, "Vinicius", 15.70, 1130, "001")
conta2 = Conta(210, "Aragorn", 761.92, 3200, "001")

conta.extrato()
conta.saca(1145.70)
conta.extrato()
