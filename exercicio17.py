num = int(input("Insira o primeiro numero: "))
num1 = int(input("Insira o segundo numero: "))
num2 = int(input("Insira o terceiro numero: "))
if (num < num1 + num2 or num1 < num + num2 or num2 < num1 + num):
    if(num == num1 == num2):
        print("Esse Triangulo é escaleno")
    else:
        print("Esse Triangulo não é Valido")
elif(num == num1 != num2 or num == num2 != num1 or num1 == num != num2 or num1 == num2 != num or num2 == num != num1 or num2 == num1 != num):
    print("Triangulo isoseles")
elif(num != num1 != num2):
    print("Esse triangulo é escaleno")