"""Exemplos de funções"""

"""
f(x) = 5 * (x / 2) #funcão simples comum
"""
#Principio de responsabilidade única (Solid - Single Responsability) #Uma função deve resolver apenas um problema, se tiver que resolver mais outra fórmula, tem que criar outra função

#função traduzida para Python

#(def) definition - define uma função
def f(x): #assinatura da função
    result = 5 * (x / 2) #Toda função em python tem que ter um return, se não tiver, sempre vai retornar None
    ...
    return result

def double (x):
    return x * 2

valor = double (f(10))


print(valor)
print(valor == 50)

###


def print_in_upper(text):
    """Procedure with no explicit return"""
    print(text.upper())
    # implicit return None


print_in_upper("bruno")

###

def heron(a, b, c):
    """Formula de Heron calcula a area de um triangulo com lados diferentes"""
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * ( s - b) * (s - c) 
    return area ** 0.5 #math.sqrt(area)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (8, 15, 17),
    (12, 35, 37)
]

for t in triangulos:
    area = heron(t[0], t[1], t[2])
    print(f"A area do triangulo é: {area}")

###
funçao é uma variavel, diferença que usamos o def