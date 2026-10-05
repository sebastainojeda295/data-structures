from random import randint
import os
numbers = []
status = True

while status:
    num = randint (1,100)

    if num in numbers:
        print(f"numero generad: {num}")
        print("Este número ya está registrado en la lista.")
    else:
        numbers.append(num)
    

    print (f"Lista de visualización: {numbers}")
    print (f"Total de filas: {len (numbers)}")

    
    while True:
        key = input("Quieres introducir otro número? [y/Y/n/N] ")
        if key in ['Y', 'y', 'N', 'n']:
            break
        print("Opción inválida. Por favor, introduzca Y, y, N, or N, n")

    if key == 'N' or key == 'n':
        print("Programa finalizado.")
        break
        
    
