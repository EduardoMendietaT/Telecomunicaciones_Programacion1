'''
Cree código de tal manera que 2 valores: x y y sean ingresados mediante el teclado. 
Realizar varias comparaciones lógicas y matemáticas, muestre los resultados.
'''
x = int(input('\nIngrese un número[x]: '))
y = int(input('Ingrese otro número[y]: '))

# 1. Operaciones lógicas con las variables x e y.
print('\nx > y: ', x > y, ', x < y: ', x < y, '.')
print('x >= y: ', x >= y, ', x <= y: ', x <= y, '.')
print('x == y: ', x == y, ', x != y: ', x != y, '.')
print(f'{x} o {y} mayor a 10: {x > 10 or y > 10}')
print(f'{x} >= 0 y {y} <= 10: {x >= 0 and y <= 10}.')
print(f'{x} no es {y}: {x is not y}.\n')

# 2. Operaciones matemáticas con x e y.
print(f'{x} // {y} = {x // y}')
print(f'{x} % {y} = {x % y}')
print(f'{x} + {y} - {y} ** {2} = {x + y - y**2}')
print(f'({x} + {y}) / ({x} - {y}) = {(x + y) / (x - y)}')
print(f'({x} - {y})**2 = {(x - y)**2}')
print(f'({x}/{y} + {x}) - {y}/{x} = {x/y + x - y/x}')