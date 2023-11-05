import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, "../codigo"))

from bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_23(self):
        entrada = "13/03/2000"  # Given (Contexto)
        esperado = 23

        funcionario_teste = Funcionario("Teste", entrada, 1111)

        resultado = funcionario_teste.idade()  # When (Ação)

        assert resultado == esperado  # Then (Desfecho)

    def test_quando_sobrenome_recebe_Vinicius_Martins_Freire_deve_retornar_Freire(self):
        entrada = "Vinicius Martins Freire"  # Given (Contexto)
        esperado = "Freire"

        lucas = Funcionario(entrada, "05/09/2001", 1111)

        resultado = lucas.sobrenome()  # When (Ação)

        assert resultado == esperado  # Then (Desfecho)

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada = 100000  # Given (Contexto)
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "05/09/2001", entrada)

        funcionario_teste.decrescimo_salario()  # When (Ação)
        resultado = funcionario_teste.salario()

        assert resultado == esperado  # Then (Desfecho)
