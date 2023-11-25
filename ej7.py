def es_primo(numero):
    #menores o iguales a 1 no son primos
    if numero <= 1:
        return False
    #divisibilidad desde 2 hasta la raíz cuadrada del número puesto
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

#ejemplo
numero_evaluar = int(input("Ingrese un número para verificar si es primo: "))

if es_primo(numero_evaluar):
    print(f"{numero_evaluar} es un número primo.")
else:
    print(f"{numero_evaluar} no es un número primo.")
