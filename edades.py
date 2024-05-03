import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("edades.csv") # Lee el archivo CSV
df['age'] = pd.to_datetime(df['age'], format='%d/%m/%Y') # Convierte la columna 'age' a datetime
df = df[df['age'] <= pd.Timestamp.now() - pd.DateOffset(years=25)] # Filtra las edades menores o iguales a 25


df = df.sort_values(by='age') # Ordena las edades de menor a mayor


age_counts = df['age'].dt.year.value_counts().sort_index() # Cuenta el número de personas por año


result_df = pd.DataFrame({'Edades': age_counts.index, 'Frecuencia': age_counts.values}) # Crea el DataFrame

print(result_df) # Imprime el DataFrame


plt.plot(result_df['Edades'], result_df['Frecuencia'], marker='o', linestyle='-') # Grafica la frecuencia de edades
plt.title('Frecuencia de Edades') # Agrega un título
plt.xlabel('Edades') # Agrega una etiqueta al eje x
plt.ylabel('Frecuencia') # Agrega una etiqueta al eje y
plt.grid(True) # Agrega una cuadrícula
plt.show() # Muestra el gráfico