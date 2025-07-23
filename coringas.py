#sabendo os dados que serão passados
"""
def soma(a, b):
    return a + B

soma(1,3)
soma(1, b=3)

def hello(nome, sobrenome="Sabugosa"):
    print(f"Hello {nome}, {sobrenome}")

hello("Bruno", "Rocha")
hello("Bruno", sobrenome="Rocha")
hello(sobrenome="Rocha", nome="Rocha")
hello("bruno")
def funcao()
"""
#Quando nao sabemos o que o usuario vai passar (exemplo, a funcao 'PRINT')
def funcao(*args, timeout=10, **options):
    for item in args:
        print(item)

    print(options)
    print(f"timeout {timeout}")

funcao(
    "Bruno", 
    1, 
    True, 
    timeout=90, 
    nome="Joao", 
    cidade="Viana", 
    data="hoje",
    banana=1,
    panela=3,
    teclado=True,
)