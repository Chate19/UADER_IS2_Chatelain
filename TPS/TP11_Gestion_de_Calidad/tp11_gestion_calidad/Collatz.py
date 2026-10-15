# Calculando el número de iteraciones del algoritmo de Collatz
def collatz(num):
    iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        iteraciones += 1
    return iteraciones

# Comprobando los resultados
try:
    i = int(input("Ingrese un numero entero positivo (maximo 1999): "))
    if i <= 0:
        print("Error: El numero debe ser mayor a 0.")
    elif i > 1999:
        print("Error: El numero supera el limite maximo a validar (1999).")
    else:
        # Se imprime el numero de partida y las iteraciones
        print("El numero de iteraciones para %d es %d\n" % (i, collatz(i)))
except ValueError:
    print("Error: Debe ingresar un valor numerico entero.")