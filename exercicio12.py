num = int(input("Insira um numero: "))

tot = num % 3
tot1 = num % 7

if(tot == 0 and tot1 == 0):
    print("é divisivel")
else:
    print("não é divisivel")

