def factorial(numero):
    #factorial de 0 y 1 es 1
    if numero == 0 or numero == 1:
        return 1
    #factorial para numeros mayores que 1
    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado

#ejemplo
numero_evaluar = int(input("Poner un numero entero no negativo para calcular el factorial: "))

if numero_evaluar < 0:
    print("Poner un numero entero no negativo.")
else:
    resultado_factorial = factorial(numero_evaluar)
    print(f"El factorial de {numero_evaluar} es: {resultado_factorial}")
