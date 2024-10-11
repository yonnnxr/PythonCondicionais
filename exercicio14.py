nome = str(input("Insira o seu numero: "))
not1 = float(input("Insira a primeira nota: "))
not2 = float(input("insira a segunda nota: "))
not3 = float(input("insira a terceira nota: "))
tot = (not1 + not2 + not3) / 3
print(nome)
if(tot >= 7.0):
    print("Aprovado")
elif(tot <= 5):
    print("reprovado")
else:
    print("Voce esta de recuperacao")