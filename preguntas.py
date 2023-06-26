"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    with open('data.csv', 'r') as file:
        total = 0
        for line in file:
            columns = line.strip().split('\t')
            total += int(columns[1])
    return total

# Resultado: 214


def pregunta_02():
    with open('data.csv', 'r') as file:
        count_dict = {}
        for line in file:
            columns = line.strip().split('\t')
            letter = columns[0]
            count_dict[letter] = count_dict.get(letter, 0) + 1
    sorted_counts = sorted(count_dict.items())
    return sorted_counts

# Resultado:
# [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]


def pregunta_03():
    with open('data.csv', 'r') as file:
        sum_dict = {}
        for line in file:
            columns = line.strip().split('\t')
            letter = columns[0]
            value = int(columns[1])
            sum_dict[letter] = sum_dict.get(letter, 0) + value
    sorted_sums = sorted(sum_dict.items())
    return sorted_sums

# Resultado:
# [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]


def pregunta_04():
    with open('data.csv', 'r') as file:
        month_counts = {}
        for line in file:
            columns = line.strip().split('\t')
            date = columns[2]
            month = date.split('-')[1]
            month_counts[month] = month_counts.get(month, 0) + 1
    sorted_counts = sorted(month_counts.items())
    return sorted_counts

def pregunta_05():
    letters = []
    count = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for line in file:
            if not line[0] in letters:
                letters.append(fila[0])
                count.append([int(fila[1])])
            else:
                count[letras.index(fila[0])].append(int(fila[1]))

    out = []

    for letter in sorted(set(letras)):
        out.append((letter, max(count[letters.index(letter)]), min(count[letters.index(letter)])))
    
    return out

def pregunta_06():
    cadenas = []
    valores = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            diccionario = fila[4].split(',')

            for elemento in diccionario: 
                cadena = elemento.split(':')[0]
                valor = elemento.split(':')[1]

                if cadena not in cadenas:
                    cadenas.append(cadena)
                    valores.append([int(valor)])
                else:
                    valores[cadenas.index(cadena)].append(int(valor))

    salida = []

    for cadena in sorted(cadenas):
        salida.append((cadena, min(valores[cadenas.index(cadena)]), max(valores[cadenas.index(cadena)])))

    return salida

def pregunta_07():
    numeros = []
    letras = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            if int(fila[1]) not in numeros:
                numeros.append(int(fila[1]))
                letras.append([fila[0]])
            else:
                letras[numeros.index(int(fila[1]))].append(fila[0])

    salida = []

    for numero in sorted(numeros):
        salida.append((numero, letras[numeros.index(numero)]))

    return salida

def pregunta_08():
    numeros = []
    letras = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            if int(fila[1]) not in numeros:
                numeros.append(int(fila[1]))
                letras.append({fila[0]})
            else:
                letras[numeros.index(int(fila[1]))].add(fila[0])

    salida = []

    for numero in sorted(numeros):
        salida.append((numero, list(sorted(letras[numeros.index(numero)]))))

    return salida

def pregunta_09():
    salida = {}

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            diccionario = fila[4].split(',')

            for elemento in diccionario: 
                cadena = elemento.split(':')[0]

                if cadena not in salida.keys():
                    salida[cadena] = 1
                else:
                    salida[cadena] += 1

    return dict(sorted(salida.items()))

def pregunta_10():
    salida = []

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            col4 = len(fila[3].split(','))
            col5 = len(fila[4].split(','))
            salida.append((fila[0], col4, col5))
    
    return salida

def pregunta_11():
    letras = {}

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            for letra in fila[3].split(','):
                if not letra in letras.keys():
                    letras[letra] = int(fila[1])
                else:
                    letras[letra] += int(fila[1])

    return dict(sorted(letras.items()))


def pregunta_12():
    letras = {}

    with open('data.csv') as csv_file:
        datos = csv.reader(csv_file, delimiter='	')
        for fila in datos:
            letra = fila[0]
            
            for elemento in fila[4].split(','):
                numero = int(elemento.split(':')[1])

                if not letra in letras.keys():
                    letras[letra] = numero
                else:
                    letras[letra] += numero

    return dict(sorted(letras.items()))

