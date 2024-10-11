idade = int(input("Digite a idade do nadador: "))

if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10:
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
elif 18 <= idade <= 25:
    categoria = "Sênior"
else:
    categoria = "Idade fora da faixa etária"

print(f"O nadador pertence à categoria: {categoria}")