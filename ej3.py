numeros_ingresados = []

# Inicializar contadores
pares = 0
impares = 0

# Bucle while
while True:
    respuesta = input("¿Desea ingresar un número? (SI/NO): ").upper()
    
    if respuesta != "SI":
        break
    
    try:
        #ingrese un número
        numero = int(input("Ingrese el número: "))
        
        numeros_ingresados.append(numero)
        
        # Evaluar si el número es par o impar y actualizar los contadores
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    except ValueError:
        # no ingresa un número válido
        print("Por favor, ingrese un número entero válido.")

print("Números ingresados:", numeros_ingresados)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)

