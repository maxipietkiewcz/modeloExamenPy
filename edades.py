import pandas as pd


df = pd.read_csv("edades.csv") # Lee el archivo CSV
df['age'] = pd.to_datetime(df['age'], format='%d/%m/%Y') # Convierte la columna 'age' a datetime
df = df[df['age'] <= pd.Timestamp.now() - pd.DateOffset(years=25)] # Filtra las edades menores o iguales a 25


df = df.sort_values(by='age') # Ordena las edades de menor a mayor


age_counts = df['age'].dt.year.value_counts().sort_index() # Cuenta el número de personas por año


result_df = pd.DataFrame({'Edades': age_counts.index, 'Frecuencia': age_counts.values}) # Crea el DataFrame

print(result_df) # Imprime el DataFrame
