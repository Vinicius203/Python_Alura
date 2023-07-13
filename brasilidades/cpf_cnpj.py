from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return Doccpf(documento)
        elif len(documento) == 14:
            return Doccnpj(documento)
        else:
            raise ValueError("A quantidade de dígitos está incorreta!")


class Doccpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("Esse CPF é inválido!")

    def valida(self, documento):
        validador = CPF()
        return validador.validate(documento)

    def formata(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.formata()


class Doccnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("Esse CNPJ é inválido!")

    def valida(self, documento):
        validador = CNPJ()
        return validador.validate(documento)

    def formata(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.formata()
