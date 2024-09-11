numero = int(input("Digite um número: "))
valor = int(input("Digite outro número: "))

if numero > valor:
    print(f"O primeiro número {numero} é MAIOR que {valor}")
elif numero < valor:
    print(f"O primeiro número {numero} é MENOR que {valor}!")
else:
    print(f"Os números são IGUAIS!")