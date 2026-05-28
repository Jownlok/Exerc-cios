km_percorrido = int(input('Digite a quantidade de kms percorridos: '))
quantidade_dias = int(input('Digite a quantidade de dias alugados:'))

valor_km = km_percorrido * 0.15
valor_dias = quantidade_dias * 60
valor_final = valor_km + valor_dias

print(f'O valor total a ser pago pelo uso do carro é de R$: {valor_final: .2f}')
