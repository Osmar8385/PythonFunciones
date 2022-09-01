# Escribe tus funciones abajo de esta línea

def main():
    # Escribe tu código abajo de esta línea
def Pies_cm(opcion):
    pies = cantidad * 30.48
    return pies

def Pulgadas_cm(opcion):
    pulgadas = cantidad * 2.54
    return pulgadas

def Yardas_cm(opcion):
    yardas = cantidad * 90.44
    return yardas

print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')

opcion=int(input('Introduce una opción:'))

cantidad=int(input('Introduce una cantidad:'))

if opcion == 1:
    print("Son:", Pies_cm(opcion), "pies")
    
elif opcion == 2:
    print("Son:", Pulgadas_cm(opcion), "pulgadas")
    
elif opcion == 3:
    print("Son:", Yardas_cm(opcion), "yardas")
    
elif opcion != 1:
    print("Error")
    
elif opcion != 2:
    print("Error")
    
elif opcion != 3:
    print("Error")

if __name__ == '__main__':
    main()
