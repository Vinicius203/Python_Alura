from validate_docbr import CPF, CNPJ


class CPF_CNPJ:
    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)

        if self.tipo_documento == "cpf":
            if self.valida_cpf(documento):
                self.cpf = documento
            else:
                raise ValueError("O CPF é inválido!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_eh_Valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("O CNPJ é inválido!")
        else:
            raise ValueError("Esse tipo de documento é inválido!")

    def valida_cpf(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("A quantidade de dígitos está incorreta!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()

    def valida_cnpj(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("A quantidade de dígitos está incorreta!")
