# Documentación del Script Complejo en Python: Análisis Estadístico y Visualización

Este documento contiene el código Python completo y su explicación detallada para realizar análisis de datos cuantitativos, generación de tablas estilizadas en consola y gráficos estadísticos de alta calidad.

## Estructura del Archivo

- **Nombre del archivo sugerido:** `analisis_estadistico_avanzado.py`
- **Ubicación en el repositorio:** `/python/analisis_estadistico_avanzado.py`

## Requisitos Previos (Librerías)

Para ejecutar este script, es necesario instalar las librerías estadísticas y de visualización habituales:

```bash
pip install pandas numpy matplotlib seaborn tabulate
```

## Código Completo del Script (`analisis_estadistico_avanzado.py`)

> **Script:** `analisis_estadistico_avanzado.py`
> **Propósito:** Demostración de análisis de datos complejo en Python (Alternativa a SPSS)
>
> **Incluye:**
>
> 1. Generación y manipulación de DataFrames con Pandas.
> 2. Tablas de resumen estadístico estructuradas.
> 3. Análisis bivariado y contraste de grupos (Análisis Descriptivo y Agrupado).
> 4. Visualización con Matplotlib y Seaborn (Histogramas, Boxplots y Diagramas de Dispersión).

## Explicación de los Módulos del Código

| Función / Módulo            | Funcionalidad                                                                                                                                          | Equivalente en SPSS                             |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| `cargar_y_preparar_datos()` | Genera un dataset cuantitativo de prueba con variables numéricas y categóricas.                                                                        | Vista de datos / Importación de archivos `.sav` |
| `mostrar_tablas_resumen()`  | Utiliza pandas y tabulate para imprimir tablas formateadas con estadísticos descriptivos (media, desviación estándar, cuantiles) agrupados por factor. | `DESCRIPTIVES` / `MEANS` / `CROSSTABS`          |
| `generar_graficos()`        | Crea un panel de 4 gráficas compuestas.                                                                                                                | `GRAPH` / Generador de gráficos de SPSS         |

### Detalle del Panel de Gráficos

| Visualización           | Descripción                           |
| ----------------------- | ------------------------------------- |
| Histogramas             | Con estimación de densidad (KDE).     |
| Boxplots                | Con superposición de puntos (jitter). |
| Diagramas de dispersión | Multivariable.                        |
| Mapa de calor (heatmap) | Para matriz de correlación Pearson.   |
