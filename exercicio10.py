num = int(input("Informe um numero: "))

resto = num % 5

match resto:
    case 0:
        print("é divisivel por 5")
    case _:
        print("não é divisivel por 5")