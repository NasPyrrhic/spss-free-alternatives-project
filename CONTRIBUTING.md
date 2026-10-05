# Guía de Contribución (`CONTRIBUTING.md`)

¡Gracias por tu interés en contribuir a este repositorio de alternativas de software libre a IBM SPSS Statistics y buenas prácticas en proyectos de ingeniería! Este documento contiene las pautas y convenciones necesarias para enviar mejoras, corregir errores, añadir nuevos scripts o enriquecer la documentación del proyecto.

## Código de Conducta

Nos comprometemos a fomentar un entorno abierto, acogedor y respetuoso. Se pide a todos los colaboradores mantener una comunicación respetuosa, constructiva y profesional en todo momento.

## ¿Cómo puedo contribuir?

### 1. Reportar Errores (Bug Reports)

Si encuentras una falla en la ejecución de los scripts o algún error en las guías de instalación/documentación:

1. Revisa la sección de **Issues** para verificar que el problema no haya sido reportado previamente.
2. Abre un **New Issue** utilizando un título descriptivo.
3. Incluye información detallada:
   - Sistema operativo y versión.
   - Versión del lenguaje o software (ej. Python 3.10, R 4.3.1, GNU PSPP 2.0).
   - Pasos exactos para reproducir el error y el mensaje de salida obtenido.

### 2. Proponer Nuevas Funcionalidades o Scripts

Si deseas añadir un nuevo script de análisis (ej. prueba t de Student, ANOVA, regresiones, etc.) o incluir una nueva alternativa Open Source:

- Crea un **Issue** con la etiqueta `enhancement` antes de comenzar a programar para discutir la propuesta con el mantenedor.

## Flujo de Trabajo para Colaborar (Fork & Pull Request)

Para mantener la integridad de la rama principal (`main`), todas las contribuciones deben seguir este flujo:

### Paso 1: Realizar un Fork del Repositorio

Haz clic en el botón **Fork** en la esquina superior derecha de la página del repositorio en GitHub para crear una copia del proyecto en tu cuenta personal.

### Paso 2: Clonar tu Fork

Clona tu repositorio bifurcado localmente en tu equipo:

```bash
git clone https://github.com/TU_USUARIO/NOMBRE_REPOSITORIO.git
cd NOMBRE_REPOSITORIO
```

### Paso 3: Crear una Nueva Rama (Branch)

Crea una rama específica para la función o corrección en la que trabajarás. Evita hacer cambios directamente en `main`:

```bash
git checkout -b feature/nueva-prueba-anova

# O para correcciones de errores:
git checkout -b fix/error-script-python
```

### Paso 4: Realizar los Cambios y Commits

Escribe el código o documentación asegurándote de seguir los estándares del proyecto. Realiza commits pequeños y con mensajes claros en presente imperativo:

```bash
git add .
git commit -m "Añade script de ANOVA en Python y actualiza README"
```

### Paso 5: Enviar los Cambios a tu Fork (Push)

Sube la rama con tus cambios a tu repositorio en GitHub:

```bash
git push origin feature/nueva-prueba-anova
```

### Paso 6: Crear un Pull Request (PR)

1. Ve al repositorio original en GitHub. Verás un aviso que sugiere crear un Pull Request desde tu rama recientemente subida.
2. Haz clic en **Compare & pull request**.
3. Describe de manera clara qué cambios introduce tu PR y qué problema resuelve.
4. Vincula el PR al Issue correspondiente si aplica (ej. `Closes #12`).

## Estándares y Convenciones del Repositorio

- **Estructura de Carpetas:** Mantén los scripts organizados en la carpeta correspondiente al software utilizado (`/python/`, `/r/`, `/pspp/`, etc.).
- **Comentarios y Documentación:** Todo script o sintaxis enviada debe incluir comentarios claros en español explicando el propósito de cada sección de código.
- **Archivos README:** Si añades un nuevo software o herramienta, debes incluir o actualizar el archivo `README.md` de esa carpeta con las instrucciones de instalación y ejecución.
- **Sintaxis Limpia:** En Python, procura seguir PEP 8. En R y scripts de sintaxis SPSS, mantén una sangría clara y nombres de variables autoexplicativos.

## Proceso de Revisión

Una vez enviado tu Pull Request, el equipo o mantenedor del proyecto revisará el código. Es posible que se soliciten pequeños ajustes antes de aprobar la integración final a la rama principal (`main`). ¡Agradecemos tu paciencia y contribución!