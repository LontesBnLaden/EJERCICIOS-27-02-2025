#EJERCICIO 1


a = [int(input(f'{i+1}: ')) for i in range(5)]
b = [int(input(f'{i+1}: ')) for i in range(5)]

# Multiplicar las listas elemento a elemento
resultado = [a[i] * b[i] for i in range(5)]

# Mostrar el resultado
print('Resultado de la multiplicación:', resultado)




#EJERCICIO 2

numeros = []

for i in range(5):  # Asegurar que el bloque dentro del for esté bien indentado
    num = float(input(f'Ingrese el número {i+1}: '))
    numeros.append(num)

# Ordenar los números de menor a mayor
numeros.sort()

# Mostrar el resultado
print('Números ordenados de menor a mayor:', numeros)


#EJERCICIO 3

import numpy as np

print("Ingrese 5 números separados por espacio para la primera lista:")
a = np.array(list(map(int, input().split())))

print("Ingrese 5 números separados por espacio para la segunda lista:")
b = np.array(list(map(int, input().split())))

# Verificar que ambas listas tengan 5 elementos
if len(a) == 5 and len(b) == 5:
    resultado = a * b
    print('Resultado de la multiplicación:', resultado)
else:
    print("Error: Debes ingresar exactamente 5 números en cada lista.")



#EJERCICIO 4

a = [int(input(f'{i+1}: ')) for i in range(5)]
b = [int(input(f'{i+1}: ')) for i in range(5)]

# Multiplicar las listas elemento a elemento
resultado = [a[i] * b[i] for i in range(5)]

# Mostrar el resultado
print('Resultado de la multiplicación:', resultado)
