#definição ou atribuição
#assinatura
#documentação / docstring

#atribuição (atribuindo um valor) valor = 1
#Definição def nome_da_funcao
#assinatura + type hints - def nome_da_funcao( ) : tudo que estiver entre o parentese e os dois pontos é a assinatura, podendo ou nãor receber parametros
#codigo
#valor de retorno

# - parametros
#posicional - passados em ordem
# nomeados

# """ ... """ Esses tres aspas, tudo o que estiver entre eles será a documentação do código
# Na funçaõ é sempre bom escrever o que ela fez, em uma sentença que caiba até 79 caracteres 

def nome_da_funcao(a: int, b: int, c: int) -> int: 

    """ Esta função faz algo com a, b, c
    quando o parametro tiver o valor 10 vai acontecer x.

    :param a: Numero inteiro
    :type a: int
    :param b: Numero inteiro
    :type b: int
    :param c: Numero inteiro
    :type c: int
    :return: Retorna o resultado de a + b + c
    :rtype: int
    """

    resultado = a + b + c 
    return resultado

# passagem de argumentos nomeados
valor = nome_da_funcao(a=1, b=2, c=3)
valor = nome_da_funcao(a=1, b=2, c=3)
valor = nome_da_funcao(a=1, b=2, c=3)

#passagem de argumentos posicionais
valor = nome_da_funcao(1, 2, 3)

#passagem de argumenros mista
#argumentos posicionais tem que vir antes dos nomeados
valor = nome_da_funcao(1, 2, c=3)
valor = nome_da_funcao(1, c=2, b=3)

#funcao com muitos argumentos
valor = nome_da_funcao(
    1,
    c=2,
    b=3,
)

print(valor)

##################

def outra_funcao(a, b, c):
    """Explica o que ela faz"""
    #tupla como valor de retorno
    return a * 2, b * 2, c * 2

valor1, valor2, valor3 = outra_funcao(1, 2, 3)
print(valor1)
print(valor1)
print(valor1)

#caso queira que venha apenas um valor
valor1, *resto = outra_funcao(1, 2, 3)
print(valor1)
print(resto)

###################################

#Passagem de argumentos com desempacotamento

def soma(n1, n2):
    """Faz a soma de dois numeros."""
    return n1 + n2

#normal
print(soma(10, 20))

#argumentos em sequencia
args = (20, 30) #tupla
print(soma(args[0], args[1]))
print(soma(*args))

#um asteristicos desempacota tupla, dois asterisco desempacota mais de um valor

#argumentos dicionario / nomeados
args = {"n2": 90, "n1": 100}
print(soma(n1=args["n1"], n2=args["n2"]))
print(soma(**args))

lista_de_valores_para_somar = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 200},
    {"n2": 9, "n1": 650},
]

for item in lista_de_valores_para_somar:
    if isinstance(item, dict):
        print(soma(**item))
    else:
        print(soma(*item))
