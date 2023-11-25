def contar_digitos_en_numero(numero, digito):
    # Convertir el número a una cadena
    numero_str = str(numero)
    
    #metodo count 
    cantidad = numero_str.count(str(digito))
    
    return cantidad

numero_ingresado = 15789000
digito_evaluar = 0

resultado = contar_digitos_en_numero(numero_ingresado, digito_evaluar)

print(f"Número ingresado: {numero_ingresado} y Dígito: {digito_evaluar}")
print(f"Cantidad de veces {digito_evaluar} en el número: {resultado}")
