num = float(input("Insira um numero: "))

if(num >= 0):
    tot1 = num ** (1/2)
    print(f"a raiz de {num} é {tot1}")
else:
    tot2 = num * num
    print(f"o quadrado de {num} é {tot2}")