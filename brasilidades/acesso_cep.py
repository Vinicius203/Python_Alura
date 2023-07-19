class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError("O CEP é inválido!")

    def cep_valido(self, cep):
        if len(cep) == 8:
            return True
        return False

    def format_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    def __str__(self):
        return self.format_cep()
