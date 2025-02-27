# Ingresar dos listas de 5 números
a = [int(input(f'{i+1}: ')) for i in range(5)]
b = [int(input(f'{i+1}: ')) for i in range(5)]

# Multiplicar las listas elemento a elemento
resultado = [a[i] * b[i] for i in range(5)]

# Mostrar el resultado
print('Resultado de la multiplicación:', resultado)
