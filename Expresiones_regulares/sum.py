# Importando el modulo
import re

# Leyendo el archivo con el texto
with open("sum.txt","r") as archivo:
    texto = archivo.read()

# Buscando los numeros
numbers = re.findall('[0-9]+', texto)

# Convirtiendo cada string de la lista en int
numbers = [int(x) for x in numbers]

# Imprimiendo resultado
print(f'La suma de los numeros contenidos en el texto es igual a: {sum(numbers)}')