# Ejemplo "Hola Mundo" en Python
import pandas as pd

print("¡Hola Mundo Estadístico desde Python!\n")

datos = pd.DataFrame({
    'id': [1, 2, 3, 4, 5],
    'edad': [23, 30, 25, 42, 19],
    'puntuacion': [85.5, 92.0, 78.4, 88.1, 95.0]
})

print(datos)
print("\nEstadísticos Descriptivos:")
print(datos[['edad', 'puntuacion']].describe())