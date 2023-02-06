"""
 Cálculo do IMC
"""
nome = 'Nome'
altura = 1.55
peso = 60.50
imc = peso/(altura ** 2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
print("Acabou aqui")