def decimal_para_binario(numero):
    if numero >= 1:
        decimal_para_binario(numero // 2)
        print(numero % 2, end='')

def decimal_para_octal(numero):
    if numero >= 1:
        decimal_para_octal(numero // 8)
        print(numero % 8, end='')

def decimal_para_hexadecimal(numero):
    if numero >= 1:
        decimal_para_hexadecimal (numero // 16)
        resto = numero % 16
        if resto < 10:
            print(resto, end='')
        else:
            #chr recebe um código Unicode (valor de ASCII)e retorna o caractere correspondende; 
            # ord recebe um caractere e retorna um código Unicode (valor de ASCII);
            # Basicamente são conversores de acordo com a tabela de códigos ASCII; 
            print(chr(ord('A') + resto - 10), end='')

numero_decimal = int(input("Digite um número decimal: "))

while True:
    menu = int(input("Agora escolha a base para a conversão\n1 binário\n2 octal\n3 hexadecimal: "))
    if menu == 1:
        print(f"O número {numero_decimal} em binário é: ", end='')
        decimal_para_binario(numero_decimal)
        break
    elif menu == 2:
        print(f"o número {numero_decimal} em octal é: ", end='')
        decimal_para_octal(numero_decimal)
        break
    elif menu == 3:
        print(f"O número {numero_decimal} em hexadecimal é: ", end='')
        decimal_para_hexadecimal(numero_decimal)
        break
    else:
        print("A opção não existe ou não está disponível. Repita o processo novamente!")