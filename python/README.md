# Guía de Instalación de Python y READMEs del Repositorio

---

## 1. Guía Rápida de Instalación de Python (`/python/README.md`)

Esta carpeta contiene los scripts en Python para análisis estadístico básico utilizando la biblioteca **pandas**.

### Prerrequisitos e Instalación de Python

#### Opción A: Windows

1. Descarga el instalador oficial de Python 3.x desde [python.org/downloads](https://www.python.org/downloads/).
2. **¡CRÍTICO!** Durante la instalación, marca la casilla que dice: **"Add python.exe to PATH"** (Agregar Python al PATH).
3. Haz clic en **Install Now** y completa el proceso.

#### Opción B: macOS

1. Descarga e instala la última versión desde [python.org/downloads/macos](https://www.python.org/downloads/macos/) o usa Homebrew:

```bash
brew install python
```

#### Opción C: Linux (Ubuntu/Debian)

Abre la terminal e instala Python y el gestor de paquetes pip:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Instalación de Dependencias

Para ejecutar los scripts de esta carpeta, necesitas instalar la biblioteca **pandas**. Abre tu terminal o símbolo del sistema (CMD / PowerShell) y ejecuta:

```bash
pip install pandas
```

**(Opcional)** Si también deseas trabajar con archivos nativos de SPSS (`.sav`), instala **pyreadstat**:

```bash
pip install pyreadstat
```

### Ejecución del Código "Hola Mundo"

1. Abre una terminal en esta carpeta (`/python/`).
2. Ejecuta el script con el siguiente comando:

```bash
python hola_mundo.py
```

3. **Salida esperada:** La terminal mostrará una tabla con el DataFrame de prueba y los estadísticos descriptivos básicos (media, desviación estándar, mínimos y máximos) equivalentes a los generados por SPSS.

---
