def pertence_a_fibonacci(numero):
    if numero < 0:
        return False
    
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

def gerar_fibonacci_ate(numero):
    fibonacci_numeros = []
    a, b = 0, 1
    while a <= numero:
        fibonacci_numeros.append(a)
        a, b = b, a + b
    return fibonacci_numeros

def gerar_fibonacci():
    fibonacci_numeros = []
    a, b = 0, 1
    while a <= 1000000:
        fibonacci_numeros.append(a)
        a, b = b, a + b
    return fibonacci_numeros

def main():
    fibonacci_numeros = gerar_fibonacci() 
    
    while True:
        try:
            numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
            if numero in fibonacci_numeros:
                print(f"O número {numero} pertence à sequência de Fibonacci.")
                
                print("Todos os números na sequência de Fibonacci são:")
                print(fibonacci_numeros)
                
                break 
            else:
                print(f"O número {numero} não pertence à sequência de Fibonacci. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

if __name__ == "__main__":
    main()
