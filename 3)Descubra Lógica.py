print('-' * 35)
print('Descobrindo a lógica das sequências')
print('-'*35)

#QUESTÃO A
print('A) 1, 3 ,5 ,7, __')
primeiro_termo = 1
razao = 2
quinto_termo = primeiro_termo + (5-1) * razao
for c in range(primeiro_termo, quinto_termo + razao, razao):
    print(f' -> {c}', end= '')

print('\nLógica: são números ímpares\n')
print('-'*50)

#QUESTÃO B
print('B) 2, 4, 8, 16, 32, 64, __')
a1 = 2
raz = 2
set_termo = 7
for a in range(set_termo):
    t = a1 *(raz ** a)
    print(f' -> {t}', end = '')
print('\nLógica: potência de 2\n')

#QUESTÃO C
print('-'*50)
print('C) 0, 1, 4, 9, 16, 25, 36, __')

for b in range(0, 8):
    print(f'-> {b} * {b} = {b*b} ')
print('Lógica: Quadrado perfeito\n')

#QUESTÃO D
print('-'*50)
print('D) 4, 16, 36, 64, __')
for z in range(2, 12, 2):
    print(f'-> {z}² = {pow(z,2)}')
print('Lógica: Os números pares elevado a 2\n')

#QUESTÃO E
print('-'*50)
print('E) 1, 1, 2, 3, 5, 8, __')
t7 = 5
t1 = 0
t2 = 1
cont = 0
while cont <= t7:
    t3 = t1 + t2
    print(f'-> {t3} ', end='')
    t1 = t2
    t2 = t3
    cont += 1
print('\nLógica: Sequência fibonacci\n')

#QUESTÃO F
print('-'*50)
print('F) 2,10, 12, 16, 17, 18, 19, __')
print('200')
print('\nLógica: Números que começam com a letra D(dois, dez...)')
