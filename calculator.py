"""
Calculadora Básica em Python - Entrega 1
Funções: adição, subtração, multiplicação, divisão
Projeto didático para aprendizado de programação e engenharia de software
"""

def adicionar(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtrair(a, b):
    """Retorna a subtração de b de a."""
    return a - b

def multiplicar(a, b):
    """Retorna a multiplicação de a por b."""
    return a * b

def dividir(a, b):
    """Retorna a divisão de a por b. Lança erro se b for zero."""
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

def main():
    print("Calculadora Básica - Entrega 1")
    while True:
        entrada = input("Digite o primeiro número (ou 'sair' para encerrar): ")
        if entrada.lower() == 'sair':
            print("Encerrando a calculadora.")
            break
        try:
            a = float(entrada)
        except ValueError:
            print("Número inválido. Tente novamente.")
            continue

        operador = input("Digite o operador (+, -, *, /): ")
        try:
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Número inválido. Tente novamente.")
            continue

        try:
            if operador == '+':
                resultado = adicionar(a, b)
            elif operador == '-':
                resultado = subtrair(a, b)
            elif operador == '*':
                resultado = multiplicar(a, b)
            elif operador == '/':
                resultado = dividir(a, b)
            else:
                print("Operador inválido. Use +, -, * ou /.")
                continue
            print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    main()
