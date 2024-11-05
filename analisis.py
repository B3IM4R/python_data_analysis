import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('ventas_tienda.csv')

# Definir el orden correcto de los meses
meses_orden = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]

# Convertir la columna "Mes" en una categoría con el orden especificado
df['Mes'] = pd.Categorical(df['Mes'], categories=meses_orden, ordered=True)

# Primer gráfico: Barras de ventas por categoría
plt.figure(figsize=(10, 6))
df.groupby('Categoria')['Ventas'].sum().plot(kind='bar', color='skyblue')
plt.title('Ventas Totales por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Ventas')
plt.show()

# Segundo gráfico: Línea de ventas mensuales
plt.figure(figsize=(10, 6))
df.groupby('Mes')['Ventas'].sum().plot(kind='line', marker='o', color='coral')
plt.title('Ventas Totales por Mes')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.show()

# Tercer gráfico: Gráfico de dispersión de cantidad vs satisfacción del cliente
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Cantidad', y='SatisfaccionCliente', hue='Categoria', s=100)
plt.title('Cantidad Vendida vs Satisfacción del Cliente por Categoría')
plt.xlabel('Cantidad Vendida')
plt.ylabel('Satisfacción del Cliente')
plt.legend(title='Categoría')
plt.show()

# Cuarto gráfico: Mapa de calor de las ventas por mes y categoría
plt.figure(figsize=(10, 6))
ventas_pivot = df.pivot_table(values='Ventas', index='Mes', columns='Categoria', aggfunc='sum')
ventas_pivot = ventas_pivot.reindex(meses_orden)  # Reordenar los meses en el índice del pivot
sns.heatmap(ventas_pivot, annot=True, fmt=".0f", cmap="YlGnBu")
plt.title('Mapa de Calor de Ventas por Mes y Categoría')
plt.xlabel('Categoría')
plt.ylabel('Mes')
plt.show()