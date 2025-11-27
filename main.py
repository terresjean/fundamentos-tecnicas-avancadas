main.py
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

def menu():
    print("\n===== CALCULADORA PYTHON =====")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido! Digite um número.")

def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Encerrando o programa. Até mais!")
            break

        if opcao not in ["1", "2", "3", "4"]:
            print("Opção inválida! Tente novamente.")
            continue

        num1 = obter_numero("Digite o primeiro número: ")
        num2 = obter_numero("Digite o segundo número: ")

        if opcao == "1":
            resultado = somar(num1, num2)
        elif opcao == "2":
            resultado = subtrair(num1, num2)
        elif opcao == "3":
            resultado = multiplicar(num1, num2)
        else:
            resultado = dividir(num1, num2)

        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()
