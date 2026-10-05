# Repositorio de Alternativas Open Source a IBM SPSS Statistics

Este repositorio recopila documentación, guías de inicio rápido y scripts sencillos de prueba (ejemplos tipo "Hola Mundo") para las principales alternativas libres y de código abierto a IBM SPSS Statistics.

## Propósito del Proyecto

Facilitar la transición desde entornos estadísticos propietarios y privativos hacia herramientas de software libre, evaluando tanto opciones de interfaz gráfica (GUI) como plataformas basadas en programación.

## Software Incluido

### 1. Alternativas basadas en Interfaz Gráfica (Sin Programación)

#### jamovi

- **Descripción:** Hoja de cálculo estadística de tercera generación, intuitiva y rápida, diseñada sobre la base de R.
- **Puntos clave:** Resultados dinámicos e interactivos en tiempo real, interfaz limpia e integración transparente con R.
- **Sitio Web y Descargas:** <https://www.jamovi.org/download.html>

#### JASP

- **Descripción:** Software diseñado por la Universidad de Ámsterdam con un formato familiar y cercano al flujo tradicional de SPSS.
- **Puntos clave:** Soporte avanzado de análisis bayesianos y frecuentes, salidas visuales elegantes listos para publicación.
- **Sitio Web y Descargas:** <https://iasp-stats.org/download/>

#### GNU PSPP

- **Descripción:** El reemplazo libre oficial del proyecto GNU para IBM SPSS.
- **Puntos clave:** Clona la interfaz de usuario, los menús de navegación y el lenguaje de sintaxis de SPSS. Lee y escribe archivos nativos `.sav` y `.por` sin restricciones de licencias.
- **Sitio Web y Descargas:** <https://www.gnu.org/software/pspp/get.html>

#### RCommander (Rcmdr)

- **Descripción:** Entorno gráfico básico en menús desplegables construido sobre el lenguaje R.
- **Puntos clave:** Puente idóneo para usuarios que desean la comodidad de menús pero quieren aprender la sintaxis nativa de R.
- **Sitio Web y Descargas:** <https://www.rcommander.com/>

### 2. Alternativas basadas en Lenguajes de Programación

#### R + RStudio (Posit Desktop)

- **Descripción:** El estándar de la industria científica para computación estadística, análisis cuantitativo y gráficos de alta precisión.
- **Puntos clave:** Ecosistema infinito de paquetes (CRAN), máxima flexibilidad y reproducibilidad.
- **Sitio Web y Descargas:**
  - R Project: <https://www.r-project.org/>
  - Posit Desktop / RStudio: <https://posit.co/download/rstudio-desktop/>

#### Python (Ecosistema Científico)

- **Descripción:** Lenguaje de programación multipropósito potenciado con librerías estadísticas especializadas (pandas, scipy, statsmodels, seaborn).
- **Puntos clave:** Excelente para el manejo de datos masivos, machine learning e integración con producción.
- **Sitio Web y Descargas:** <https://www.python.org/downloads/>

## Tabla Comparativa Rápida

| Software | Tipo de Interfaz | Curva de Aprendizaje | Compatibilidad .SAV |
|---|---|---|---|
| jamovi | Gráfica (GUI) | Muy baja | Sí |
| JASP | Gráfica (GUI) | Muy baja | Sí |
| GNU PSPP | Gráfica / Sintaxis SPSS | Muy baja | Nativa (100%) |
| RCommander | Gráfica (GUI básica para R) | Baja | Sí (vía librerías) |
| R / RStudio | Código / Scripting | Media - Alta | Sí (vía haven) |
| Python | Código / Scripting | Media - Alta | Sí (vía pyreadstat) |

## Estructura del Repositorio

```
README.md          # Documentación general y resumen
jamovi/            # Guía de uso y scripts en R integrados
jasp/              # Ejemplos y datasets de prueba
pspp/              # Scripts de sintaxis (.sps)
rcommander/        # Guía de instalación e integración con R
r/                 # Scripts sencillos en R (.R)
python/            # Notebooks y scripts en Python (.py / .ipynb)
```

---
