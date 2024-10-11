nivel = int(input("Digite o nível do professor (1, 2 ou 3): "))
horas_aula = float(input("Digite o número de horas/aula dadas: "))

if nivel == 1:
    valor_hora = 12.00
elif nivel == 2:
    valor_hora = 17.00
elif nivel == 3:
    valor_hora = 25.00
else:
    print("Nível inválido!")
    exit()

salario = horas_aula * valor_hora
print(f"O salário do professor é R$ {salario:.2f}")