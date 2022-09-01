# Escribe tus funciones abajo de esta línea

def main():
    # Escribe tu código abajo de esta línea
   def area(base,altura):
    return base*altura
def volumen_prisma(base, altura, profundidad):
    return area(base,altura)*profundidad

b = float(input("Dame la base: "))
a = float(input("Dame la altura: "))
p = float(input("Dame la profundidad: "))

r = volumen_prisma(b, a, p)

print("El volumen del prisma es:",r)

if __name__ == '__main__':
    main()

