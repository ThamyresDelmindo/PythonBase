def transforma_em_maiusculo(texto):
    return texto.upper()


def transforma_em_minusculo():
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


def faz_algo(valor, funcao):
    print(f"Aplicando {funcao} em {valor}")
    return funcao(valor)


names = ["Bruno", "Joao", "Bernardo", "Cintia", "Marcia", "Juca"]

print(sorted(names, key=len)) #ordenar pelo tamanho dos nomes

print(sorted(names, key=lambda name: name.count("i"))) #ordenar por quantidade de letra

print(list(filter(lambda name: name[0].lower() == "b", names)))

print(list(map(lambda name: "Hello " + name, names)))

#Calculadora

operacao = input("operacao: [sum, mul, div, sub]:")
n1 = input("n1:").strip()
n2 = input("n2:").strip()

operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

resultado = operacoes[operacao] (int(n1), int(n2))

print(f"O resultado é: {resultado}")

#lambda só funciona com expressões, não se usa return não se chama ela, se define. 
#Pra chamar tem que passar ela como argumento com uma expressão (lambda a: a + 1) (10)
#só pode usar uma única expressão, não pode quebrar linha, só uma linha simples de código
#lambda e def são a mesma coisa, só muda o jeito de escrever, os dois são função