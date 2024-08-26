numero = int(input("Digite um número:"))
escolha = int(input("Digite\n1 para Binário\n2 para Octal\n3 para Hexadecimal:"))

if escolha == 1:
    binario = bin(numero)
    print(f"O número que você digitou foi {numero} e a conversão dele é \33[0;32;40m {binario} \33[m!")
elif escolha == 2:
    octal = oct(numero)
    print(f"O número que você digitou foi {numero} e a conversão dele é {octal}!")
else:
    hexadecimal = hex(numero)
    print(f"O número que você digitou foii {numero} e a conversão dele é {hexadecimal}!")
