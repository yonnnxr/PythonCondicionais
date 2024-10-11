num = int(input("Insira o primeiro numero: "))
num1 = int(input("Insira o segundo numero: "))
num2 = int(input("Insira o terceiro numero: "))

if (num < num1 < num2):
    print(f"{num},{num1},{num2}")
elif(num < num2 < num1):
    print(f"{num},{num2},{num1}")
elif(num1 < num2 < num):
    print(f"{num1},{num2},{num}")
elif(num1 < num < num2):
    print(f"{num1},{num},{num2}")
elif(num2 < num < num1):
    print(f"{num2},{num},{num1}")
elif(num2 < num1 < num2):
    print(f"{num2},{num1},{num2}")