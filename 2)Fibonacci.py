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

n = int(input('Digite um número: '))

if fibonacci(n):
    print(f'\nO número {n} pertencia a sequência de Fibonacci.')
else:
    print(f'\nO número {n} não pertence a sequência de Fibonacci.')