names = [  
    "Bruno", 
    "Joao", 
    "Bernardo", 
    "Barbara", 
    "Brian",
]

 
""" Como fariamos
for name in names:
    if name.lower().startswith("b"):
        print(name)
"""
# TODO: Usar lambdas

"""Agora usando funcao. Da pra usar essas duas formas"""
def starts_with_b(text):
    return text[0].lower() == "b"
    #return text.startswith(("b", "B"))

print(*list(filter(starts_with_b, names)))