'''
Cree código de tal manera que 2 valores: x e y sean ingresados mediante el teclado. 
Realizar varias comparaciones lógicas y matematicas mostrar los resultados.
'''
x = int(input("Ingrese un  número entero: "))
y = int(input("Ingrese otro  número entero: "))

# Operaciones lógicas con x e y
print('\n----------------- OPERACIONES LÓGICAS -----------------')
print(f'{x} == {y} es: {x == y}')
print(f'{x} != {y} es: {x != y}')
print(f'{x} o {y} son mayores que 10:{x > 10 or y > 10}')
print(f'{x} y {y} son menores que 10:{x < 10 and y < 10}')
print(f'{x} no es mayor que 10:{not x > 10}')

# Operaciones matematicas con x e y
print('\n----------------- OPERACIONES MATEMÁTICAS -----------------')
print(f'({x} * {y})/2 = {x * y / 2}')
print(f'({x} - {y})^2 = {(x - y)**2}')
print(f'{x}^2 + {y}^3 = {x**2 + y**3}')
print(f'{x} // {y} = {x // y}')