filas = 5
# parte arriba
for i in range(filas):
    for j in range(i + 1):
        print("*", end=" ")
    print()
# parte de abajo
for i in range(filas - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
