string = input("Digite algo para ser invertido: ")

stringInvertida = ""

for i in range(len(string)-1, -1, -1):
    stringInvertida += string[i]

print("\nSeu texto invertido será:", stringInvertida)
