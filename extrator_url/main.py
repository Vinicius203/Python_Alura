# url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
url = '      '

# Sanitização da URL
url = url.replace(' ', '')

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia!")

# separa a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# busca o valor de um parâmetro
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

if indice_e_comercial != -1:
    valor = url_parametros[indice_valor:indice_e_comercial]
else:
    valor = url_parametros[indice_valor:]

print(valor)
