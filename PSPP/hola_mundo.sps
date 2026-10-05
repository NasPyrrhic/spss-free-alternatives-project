* Ejemplo "Hola Mundo" en GNU PSPP / SPSS Syntax.

DATA LIST FREE / id edad puntuacion.
BEGIN DATA.
1 23 85.5
2 30 92.0
3 25 78.4
4 42 88.1
5 19 95.0
END DATA.

VARIABLE LABELS 
  id "Identificador de Sujeto"
  edad "Edad del Participante"
  puntuacion "Puntuación de Prueba".

DESCRIPTIVES VARIABLES=edad puntuacion
  /STATISTICS=MEAN STDDEV MIN MAX.