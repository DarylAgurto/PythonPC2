lista_alumnos = []

#cantidad de alumnos
num_alumnos = int(input("Ingrese la cantidad de alumnos: "))

#Bucle
for i in range(num_alumnos):
 #nombres
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    
    calificaciones = []
    
# Bucle 2
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j + 1} para {nombre}: "))
        calificaciones.append(calificacion)
    
    # Crear un diccionario
    alumno = {"Alumno": nombre, "Notas": calificaciones}
    lista_alumnos.append(alumno)

#listado completo de alumnos
print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)
