print('-'*22)
print('Sequência de Fibonacci')
print('-'*22)

def fibonacci(z):
    x, y = 0, 1
    while y < z:
        x, y = y, x + y
    if(y == z):
        return True
    else:
        return False

n = int(input('\nDigite um número: '))
if fibonacci(n):
    print(f'O número {n} pertencia a sequencia de Fibonacci.')
else:
    print(f'O número {n} não pertence a sequencia de Fibonacci.')
