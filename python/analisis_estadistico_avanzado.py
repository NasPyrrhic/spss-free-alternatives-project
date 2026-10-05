"""
Script: analisis_estadistico_avanzado.py
Propósito: Demostración de análisis de datos complejo en Python (Alternativa a SPSS)
Incluye:
  1. Generación y manipulación de DataFrames con Pandas.
  2. Tablas de resumen estadístico estructuradas.
  3. Análisis bivariado y contraste de grupos (Análisis Descriptivo y Agrupado).
  4. Visualización con Matplotlib y Seaborn (Histogramas, Boxplots y Diagramas de Dispersión).
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

# Configuración visual de las gráficas
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'

def cargar_y_preparar_datos():
    """Genera un dataset sintético simulando un estudio cuantitativo."""
    np.random.seed(42)
    n = 100
    
    data = {
        'ID': range(1, n + 1),
        'Grupo_Tratamiento': np.random.choice(['Control', 'Experimental A', 'Experimental B'], size=n),
        'Edad': np.random.randint(18, 65, size=n),
        'Nivel_Satisfaccion': np.random.choice(['Bajo', 'Medio', 'Alto'], size=n, p=[0.2, 0.5, 0.3]),
        'Puntuacion_Pretest': np.round(np.random.normal(loc=60, scale=10, size=n), 1),
        'Puntuacion_Postest': np.round(np.random.normal(loc=75, scale=12, size=n), 1)
    }
    
    df = pd.DataFrame(data)
    # Calcular ganancia o diferencia
    df['Diferencia_Puntuacion'] = df['Puntuacion_Postest'] - df['Puntuacion_Pretest']
    return df

def mostrar_tablas_resumen(df):
    """Muestra tablas estadísticas enriquecidas en la consola."""
    print("\n" + "="*80)
    print(" 1. VISTA PREVIA DEL DATASET (Primeros 5 Registros)")
    print("="*80)
    print(tabulate(df.head(), headers='keys', tablefmt='psql', showindex=False))

    print("\n" + "="*80)
    print(" 2. ESTADÍSTICOS DESCRIPTIVOS GENERALES")
    print("="*80)
    descriptivos = df[['Edad', 'Puntuacion_Pretest', 'Puntuacion_Postest', 'Diferencia_Puntuacion']].describe().T
    descriptivos['IQR'] = descriptivos['75%'] - descriptivos['25%']
    print(tabulate(descriptivos, headers='keys', tablefmt='psql'))

    print("\n" + "="*80)
    print(" 3. COMPARATIVA DE PUNTUACIONES POR GRUPO DE TRATAMIENTO")
    print("="*80)
    resumen_grupo = df.groupby('Grupo_Tratamiento').agg(
        Muestra=('ID', 'count'),
        Edad_Media=('Edad', 'mean'),
        Pretest_Media=('Puntuacion_Pretest', 'mean'),
        Postest_Media=('Puntuacion_Postest', 'mean'),
        Diferencia_Media=('Diferencia_Puntuacion', 'mean'),
        Desviacion_Std=('Diferencia_Puntuacion', 'std')
    ).reset_index()
    print(tabulate(resumen_grupo, headers='keys', tablefmt='psql', showindex=False, floatfmt=".2f"))

def generar_graficos(df):
    """Genera y guarda un panel visual completo con seaborn y matplotlib."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Panel de Análisis Estadístico - Alternativa SPSS en Python', fontsize=16, fontweight='bold')

    # Gráfico 1: Distribuición de Puntuaciones Pre y Post (Histograma + KDE)
    sns.histplot(df['Puntuacion_Pretest'], color="skyblue", label="Pretest", kde=True, ax=axes[0, 0], alpha=0.6)
    sns.histplot(df['Puntuacion_Postest'], color="olive", label="Postest", kde=True, ax=axes[0, 0], alpha=0.5)
    axes[0, 0].set_title('Distribución Comparativa: Pretest vs Postest')
    axes[0, 0].set_xlabel('Puntuación Obtenda')
    axes[0, 0].set_ylabel('Frecuencia')
    axes[0, 0].legend()

    # Gráfico 2: Diagrama de Caja (Boxplot) por Grupo
    sns.boxplot(x='Grupo_Tratamiento', y='Diferencia_Puntuacion', data=df, palette='Set2', ax=axes[0, 1])
    sns.stripplot(x='Grupo_Tratamiento', y='Diferencia_Puntuacion', data=df, color='black', alpha=0.3, jitter=0.2, ax=axes[0, 1])
    axes[0, 1].set_title('Diferencia de Puntuación según Grupo de Tratamiento')
    axes[0, 1].set_xlabel('Grupo')
    axes[0, 1].set_ylabel('Diferencia (Postest - Pretest)')

    # Gráfico 3: Correlación Edad vs Diferencia de Puntuación por Nivel de Satisfacción
    sns.scatterplot(x='Edad', y='Diferencia_Puntuacion', hue='Nivel_Satisfaccion', size='Puntuacion_Postest',
                    sizes=(20, 200), data=df, palette='viridis', ax=axes[1, 0])
    axes[1, 0].set_title('Relación Edad vs Ganancia de Puntuación')
    axes[1, 0].set_xlabel('Edad del Participante')
    axes[1, 0].set_ylabel('Diferencia de Puntuación')

    # Gráfico 4: Matriz de Correlación (Heatmap)
    variables_num = df[['Edad', 'Puntuacion_Pretest', 'Puntuacion_Postest', 'Diferencia_Puntuacion']]
    corr_matrix = variables_num.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f", ax=axes[1, 1], cbar=True)
    axes[1, 1].set_title('Matriz de Correlación de Variables Numéricas')

    plt.tight_layout()
    
    # Guardar gráfica en disco
    nombre_imagen = "panel_analisis_estadistico.png"
    plt.savefig(nombre_imagen, dpi=300, bbox_inches='tight')
    print(f"\n[INFO] Gráfico guardado exitosamente como '{nombre_imagen}'")
    plt.show()

if __name__ == "__main__":
    datos_estudio = cargar_y_preparar_datos()
    mostrar_tablas_resumen(datos_estudio)
    generar_graficos(datos_estudio)
