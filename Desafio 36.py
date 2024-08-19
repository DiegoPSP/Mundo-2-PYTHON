print('*' * 60)
valor_casa = float(input('Digite o valor da casa que deseja comprar:R$ '))
salario = float(input('Agora digite o seu salário mensal:R$ '))
tempo = int(input('Em quantos anos você parará a casa: '))
    
def emprestimo(valor_casa,salario,tempo):
    mensalidade = valor_casa / (tempo * 12)
    if mensalidade > (salario * 30/100):
        print(f"\nInfelizmente o seu empréstimo foi\33[0;31;40m NEGADO \33[m!\n")
    else:
        print("\nParabéns o seu empréstimo foi\33[0;32;40m APROVADO \33[m!")
        print(f"A mensalidade será de R${mensalidade:.2f}.\n")

emprestimo(valor_casa,salario,tempo)
print('*' * 60)