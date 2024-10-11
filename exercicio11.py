num = int(input("Insira um numero: "))
num1 = int(input("Insira outro numero: "))
tot = num % num1

match tot:
    case 0:
        print(f"Esse numero é divisel por {num1}")
    case _:
        print("Esse numero não é divisivel")