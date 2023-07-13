from cpf_cnpj import Documento

exemplo_cnpj = "27875944000169"
documento_cnpj = Documento.cria_documento(exemplo_cnpj)
print(documento_cnpj)

exemplo_cpf = "97272791047"
documento_cpf = Documento.cria_documento(exemplo_cpf)
print(documento_cpf)
