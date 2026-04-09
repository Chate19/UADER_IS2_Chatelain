#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Verificamos si se pasó el argumento por línea de comandos
if len(sys.argv) < 2:
    # Si se omite, lo solicitamos mediante input
    try:
        entrada = input("No se informó un número. Por favor, ingrese uno: ")
        num = int(entrada)
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        sys.exit()
else:
    # Si se informó, lo tomamos de sys.argv
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Error: El argumento debe ser un número entero.")
        sys.exit()

print(f"Factorial de {num}! es {factorial(num)}")

