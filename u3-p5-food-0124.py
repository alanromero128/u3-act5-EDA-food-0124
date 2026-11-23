import pandas as pd
import matplotlib.pyplot as plt 
# Alan Romero  NC 0124
# 1. Leer el archivo CSV comida pais India 
print("\n--- DATOS LEIDOS DESDE CSV,comida india 0124")
df_food_india= pd.read_csv('indian_food.csv')
print(df_food_india)
print("\n--- Mostrar Nombre comida + ingredientes 0124")
recipes = df_food_india[['name', 'ingredients']]
print(recipes)
print("\n--- Tiempo de cocinado mostrar 10 registrar con head 0124 ---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)
