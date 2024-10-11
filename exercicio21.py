nome = input("Digite o nome do pretendente: ")
idade = int(input("Digite a idade do pretendente: "))
grupo_risco = int(input("Digite o grupo de risco (1 - Baixo, 2 - Médio, 3 - Alto): "))

if 17 <= idade <= 70:  # Verifica se a idade está na faixa permitida
    if idade <= 20:
        categoria = grupo_risco  # Categoria é igual ao grupo de risco
    elif idade <= 24:
        categoria = grupo_risco + 1
    elif idade <= 34:
        categoria = grupo_risco + 2
    elif idade <= 64:
        categoria = grupo_risco + 3
    else:  # idade >= 65
        categoria = grupo_risco + 6

    print(f"Nome: {nome}, Idade: {idade}, Categoria: {categoria}")
else:
    print(f"Nome: {nome}, Idade: {idade}, Mensagem: Idade fora da faixa permitida.")