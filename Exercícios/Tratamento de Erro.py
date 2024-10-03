def divide_numbers():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
    else:
        print(f"O resultado da divisão é: {result:.2f}")
    finally:
        print("Obrigado por usar a calculadora.")
        
    

if __name__ == "__main__":
    divide_numbers()