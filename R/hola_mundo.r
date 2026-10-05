# Ejemplo "Hola Mundo" en R
cat("¡Hola Mundo Estadístico desde R!\n\n")

datos <- data.frame(
  id = 1:5,
  edad = c(23, 30, 25, 42, 19),
  puntuacion = c(85.5, 92.0, 78.4, 88.1, 95.0)
)

print("Resumen de los datos:")
summary(datos)

cat("\nLa puntuación media es:", mean(datos$puntuacion), "\n")