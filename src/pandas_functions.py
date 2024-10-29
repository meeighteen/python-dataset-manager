import pandas as pd

# Cargar un dataset desde un archivo CSV
df = pd.read_csv('.\datasets\candy-data.csv')  # Reemplaza con la ruta correcta

# Mostrar las primeras 5 filas del dataframe
print(df.head())

# Mostrar información del dataframe
print(df.info())

# Mostrar estadísticas descriptivas
print(df.describe())

# Crear una Series
s = pd.Series([1, 2, 3, 4])

# Crear un DataFrame
data = {
    'columna1': [1, 2, 3],
    'columna2': ['a', 'b', 'c']
}

df = pd.DataFrame(data)

print(df)

# -------------------------------------------------------------------------

def function_test():
    result = 'Hola mundo'
    return result

print(function_test())
