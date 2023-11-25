def fibonacci_hasta_limite(limite):
    fibo = [0, 1]
    
    while fibo[-1] + fibo[-2] <= limite:
        fibo.append(fibo[-1] + fibo[-2])
    
    return fibo

#fibonacci hasta el 50
serie_fibonacci = fibonacci_hasta_limite(50)

print("Serie de Fibonacci hasta 50:")
print(serie_fibonacci)
