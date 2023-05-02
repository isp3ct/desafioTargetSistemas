while True:
    try:
        numero = int(input("Digite um número inteiro: "))
        break
    except ValueError:
        print("\nDigite somente números INTEIROS\n")


#Primeiro e segundo número para iniciar a sequência de Fibonacci.
fib1 = 0
fib2 = 1

while fib2 < numero:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3

if fib2 == numero:
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
