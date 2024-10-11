tipo_cliente = int(input("Digite o tipo de cliente (1 - Residência, 2 - Comércio, 3 - Indústria): "))
consumo_kwh = float(input("Digite o consumo em kWh: "))

if tipo_cliente == 1:
    valor_kwh = 0.60
elif tipo_cliente == 2:
    valor_kwh = 0.48
elif tipo_cliente == 3:
    valor_kwh = 1.29
else:
    print("Tipo de cliente inválido!")
    exit()

valor_conta = consumo_kwh * valor_kwh
print(f"O valor da conta de luz é R$ {valor_conta:.2f}")