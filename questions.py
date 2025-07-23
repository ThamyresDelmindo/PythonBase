"""funções deixam o código mais organizado
é possível colocar um ambiente isolado
"""
"""
print("Welcome to the test.")
input("When you are ready press enter")

name = input("name:")
print(f"It is nice to meet you {name}")

color = input("What is yout favorite color?")
print(f"{color} is a great color!")

input("Describe yourself")
print("admirable!")

print("Goodbye.")
"""

def welcome():
    print("Welcome to the test.")
    input("When you are ready press enter")

def ask_questions(ask_color=False):
    name = input("name:")
    print(f"It is nice to meet you {name}")

    if ask_color:
        color = input("What is yout favorite color?")
        print(f"{color} is a great color!")

    input("Describe yourself")
    print("admirable!")

def goodbye():
    print("Goodbye.")

welcome()
ask_questions()
goodbye()