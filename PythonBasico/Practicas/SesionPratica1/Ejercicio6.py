'''
Escriba un programa que convierta temperaturas de grados celsius a fahrenheit y viceversa.
Fórmula:  𝐶=(5/9)∗(𝐹−32)
Salida esperada :
    - 60°C es 140 en Fahrenheit
    - 45°F es 7 en Celsius   
'''
# Solicitamos valores numericos para transformar a grados fahrenheit y celsius.
tmp_celsius = int(input('\nIngrese un numero para calcular su equivalente en grados Fahrenheit: '))
tmp_fahrenheit = int(input('Ingrese un numero para calcular su equivalente en grados Celsius: '))

# Convertimos los valores solicitados a grados fahrenheit y celsius respectivamente.
calc_fahrenheit = int(32 + tmp_celsius/(5/9))
calc_celsius = int((5/9) * (tmp_fahrenheit - 32))

# Mostramos las conversiones por consola.
print(f'\n{tmp_celsius}°C es {calc_fahrenheit} en Fahrenheit.')
print(f'{tmp_fahrenheit}°F es {calc_celsius} en Celsius.\n')