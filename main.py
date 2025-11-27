# Programa: Calculadora Interativa
# Disciplina: Introdução à Programação de Computadores
# Autor: Jean Terres

def menu():
    print("\n========== CALCULADORA ==========")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    print("==================================")

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

# Programa principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")

