class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


conta = Conta(123, "Vinicius", 15.70, 1130)

conta.titular
print("x")
