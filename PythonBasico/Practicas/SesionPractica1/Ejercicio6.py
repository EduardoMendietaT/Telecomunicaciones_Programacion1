'''
Escriba un programa que convierta temperaturas de grados celsius a fahrenheit y viceversa.
Fórmula: C = (5/9)*(F-32).
Salida esperada :
    60°C es 140 en Fahrenheit
    45°F es 7 en Celsius
'''
tmp_celsius = float(input('\nIngrese la temperatura en grados Celsius: '))
tmp_fahrenheit = float(input('Ingrese la temperatura en grados Fahrenheit: '))

print(f'\n{tmp_celsius}°C es {tmp_celsius/(5/9)+32} en Fahrenheit.')
print(f'{tmp_fahrenheit}°F es {(5/9)*(tmp_fahrenheit-32)} en Celsius.')