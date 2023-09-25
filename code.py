import pandas as pd
df= pd.read_csv('C:/Users/54387/Downloads/cajeros.csv')

cajeros_reabastecidos_4_dias_o_mas = ((df[['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']].sum(axis=1)) >= 4).sum()

# Imprimir el resultado
print(cajeros_reabastecidos_4_dias_o_mas)
# Filtrar los cajeros que pueden ser reabastecidos al menos 4 días a la semana
filtro_4_dias_o_mas = (df[['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']].sum(axis=1)) >= 4

# Filtrar los cajeros que tienen al menos un día en fin de semana (sábado o domingo)
filtro_fin_de_semana = (df['Sábado'] == 1) | (df['Domingo'] == 1)

# Filtrar los cajeros que no tienen turno de noche (Turno noche = 0)
filtro_sin_turno_noche = (df['Turno noche'] == 0)

# Aplicar los filtros y contar los cajeros que cumplen con todas las condiciones
cajeros_cumplen_condiciones = df[filtro_4_dias_o_mas & filtro_fin_de_semana & filtro_sin_turno_noche]

# Obtener el número de cajeros que cumplen con todas las condiciones
numero_cajeros_cumplen = len(cajeros_cumplen_condiciones)

# Imprimir el resultado
print(numero_cajeros_cumplen)




# Leer el archivo CSV con la configuración adecuada para separadores de miles
transacciones = pd.read_csv('C:/Users/54387/Downloads/transacciones.csv', decimal=',')

# Filtrar las transacciones del cajero 214
transacciones_cajero_214 = transacciones[transacciones['Cajero'] == 'Cajero 214']

# Calcular el total de dinero retirado (Monto) del cajero 214
total_retirado_cajero_214 = transacciones_cajero_214['Monto'].sum()

# Imprimir el resultado
print(total_retirado_cajero_214)

# Calcular el total de dinero retirado por cada cajero en los 102 días
total_dinero_por_cajero = transacciones.groupby('Cajero')['Monto'].sum()

# Contar cuántos cajeros son rentables (total de dinero > 2200)
cajeros_rentables = len(total_dinero_por_cajero[total_dinero_por_cajero > 2200])

# Imprimir el resultado
print(cajeros_rentables)




# Filtrar las transacciones que ocurrieron en la madrugada (formato "0:0")
transacciones_madrugada = transacciones[transacciones['Hora de la transacción'].str.match(r'^[0-1]:[0-5]$|^2:[0-5][0-9]$')]

# Contar las transacciones en la madrugada
cantidad_retiros_madrugada = len(transacciones_madrugada)

# Imprimir el resultado
print(cantidad_retiros_madrugada)
