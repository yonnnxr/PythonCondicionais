sal = int(input("Insira seu salario: "))
val = int(input("Insira o valor da prestação: "))
tot = (sal * 30) / 100

if(val <= tot):
    print("o emprestimo pode ser feito")
else:
    print("o emprestimo nao pode ser feito")