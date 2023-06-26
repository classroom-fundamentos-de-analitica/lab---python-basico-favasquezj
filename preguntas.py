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

# Resultado:
# [('01', 3), ('02', 4), ('03', 2), ('04', 4), ('05', 3), ('06', 3), ('07', 5), ('08', 6), ('09', 3), ('10', 2), ('11', 2), ('12', 3)]


def pregunta_05():
    with open('data.csv', 'r') as file:
        min_max_values = {}
        for line in file:
            columns = line.strip().split('\t')
            letter = columns[0]
            value = int(columns[1])
            if letter not in min_max_values:
                min_max_values[letter] = [value, value]
            else:
                min_max_values[letter][0] = min(min_max_values[letter][0], value)
                min_max_values[letter][1] = max(min_max_values[letter][1], value)
    result = [(letter, values[1], values[0]) for letter, values in min_max_values.items()]
    return result

# Resultado:
# [('E', 9, 2), ('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3)]


def pregunta_06():
    with open('data.csv', 'r') as file:
        min_max_dict = {}
        for line in file:
            columns = line.strip().split('\t')
            dictionary = columns[4]
            key_value_pairs = dictionary.split(',')
            for pair in key_value_pairs:
                key, value = pair.split(':')
                min_max_dict[key] = min_max_dict.get(key, []) + [int(value)]
    result = {key: (min(min_max_dict[key]), max(min_max_dict[key])) for key in min_max_dict}
    return result

# Resultado:
# {'jjj': (0, 17), 'bbb': (0, 9), 'ddd': (0, 9), 'ggg': (0, 9), 'hhh': (0, 9), 'ccc': (0, 10), 'aaa': (0, 9), 'iii': (0, 9), 'eee': (0, 9), 'fff': (0, 9)}



import csv
from collections import defaultdict

def leer_archivo():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Saltar la primera fila de encabezados
        data = list(reader)
    return data

def pregunta_07():
    data = leer_archivo()
    resultado = defaultdict(list)
    for row in data:
        valor_columna_0 = row[0]
        valor_columna_1 = int(row[1])
        valor_columna_2 = int(row[2].split('-')[1])
        resultado[valor_columna_2].append(valor_columna_0)
    return list(resultado.items())

def pregunta_08():
    data = leer_archivo()
    resultado = defaultdict(list)
    for row in data:
        valor_columna_0 = row[0]
        valor_columna_1 = int(row[1])
        valor_columna_2 = int(row[2].split('-')[1])
        resultado[valor_columna_1].append(valor_columna_0)
    return list(resultado.items())

def pregunta_09():
    data = leer_archivo()
    resultado = defaultdict(int)
    for row in data:
        valores_columna_4 = row[3].split(',')
        valores_columna_5 = row[4].split(',')
        for valor_columna_5 in valores_columna_5:
            clave = valor_columna_5.split(':')[0]
            resultado[clave] += 1
    return dict(resultado)

def pregunta_10():
    data = leer_archivo()
    resultado = []
    for row in data:
        valor_columna_0 = row[0]
        cantidad_columna_4 = len(row[3].split(','))
        cantidad_columna_5 = len(row[4].split(','))
        resultado.append((valor_columna_0, cantidad_columna_4, cantidad_columna_5))
    return resultado

def pregunta_11():
    data = leer_archivo()
    resultado = defaultdict(int)
    for row in data:
        valor_columna_1 = row[0]
        suma_columna_2 = sum(int(x.split(':')[1]) for x in row[4].split(','))
        resultado[valor_columna_1] += suma_columna_2
    return dict(sorted(resultado.items()))

def pregunta_12():
    data = leer_archivo()
    resultado = defaultdict(int)
    for row in data:
        suma_columna_5 = sum(int(x.split(':')[1]) for x in row[4].split(','))
        resultado[row[0]] += suma_columna_5
    return dict(resultado)
