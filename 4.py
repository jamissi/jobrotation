faturamento_detalhado = { 'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

total = sum(faturamento_detalhado.values())

print(f'''A soma do faturamento mensal é: 
R$ {total}\n''')

print('O percentual que cada estado teve dentro deste faturamento foi: ')

for estado, faturamento in faturamento_detalhado.items():
    percentual = faturamento / total *  100
    print(f'{estado}: {percentual:.2f}%')
