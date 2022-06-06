'''
Se requiere calcular las raíces de la función f(x) = x^4 - 2x^2 - 3000. 
Utilice funciones del paquete scipy para encontrar las raíces. Para ayudar a evaluar los posibles 
rangos donde se encuentran las raices, ejecute el código acontinuación para visualizar la función en 
el rango de -10 <= x <= 10
'''
f = lambda x: x**4 - 2*x**2 - 3000

ind = np.linspace(-10, 10, 20)
fig, ax = plt.subplots(1, 1, figsize=(15, 5))

ax.plot(ind, list(map(f, np.linspace(-10, 10, 20))))
plt.show()