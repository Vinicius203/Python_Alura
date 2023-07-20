# Aqui se tem os testes para o código de validação de CPF e CNPJ

"""
from cpf_cnpj import Documento

exemplo_cnpj = "27875944000169"
documento_cnpj = Documento.cria_documento(exemplo_cnpj)
print(documento_cnpj)

exemplo_cpf = "97272791047"
documento_cpf = Documento.cria_documento(exemplo_cpf)
print(documento_cpf)
"""


# Aqui se tem a explicação de como o RegEx funciona

"""
import re

# O colchetes denomina o intervalo e as chaves a quantidade
padrao1 = "[0-9][a-z]{2}[0-9]"
texto = "123 1a2 1oo aa1 2aa9"

resposta = re.search(padrao1, texto)

# Nesse RegEx aqui o \w pega tanto letra quantos números em um intervalo {x, y}
padrao2 = "\w{5,50}@[a-z]{3,10}.com"
texto2 = "vini12@hotmail.com"

resposta2 = re.search(padrao2, texto2)
print(resposta2.group())
"""


# Aqui se tem o código para o arquivo de telefone

"""
from telefones import Telefones
import re

telefone = "552126481234"
telefone_objeto = Telefones(telefone)

# padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
# resposta = re.search(padrao,telefone)
# print(resposta.group())

print(telefone_objeto)
"""

# Aqui se tem o código para o arquivo de datas
"""
from datetime import datetime, timedelta
from datas import Datas

cadastro = Datas()
print(cadastro)

hoje = Datas()
print(hoje.tempo_cadastro())
"""

import requests
from acesso_cep import BuscaEndereco

r = requests.get("https://viacep.com.br/ws/37890000/json/")
print(r.text)
