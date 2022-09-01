# Escribe tus funciones abajo de esta línea

def main():
    # Escribe tu código abajo de esta línea
basica = 700
estandar = 900
lujo = 1500

def total_antes_descuento(tipo_silla,cantidad):
    if tipo_silla == 'B':
        total_inicial = cantidad * basica
    elif tipo_silla == 'E':
        total_inicial = cantidad * estandar
    elif tipo_silla == 'L':
        total_inicial = cantidad * lujo
    return total_inicial

def descuento(subtotal,tipo_cliente):
    if tipo_cliente == 'F':
        descuento = (subtotal*.20)
    if tipo_cliente == 'N':
        descuento = (subtotal*.10)
    return descuento

tipo_silla = input('Selecione el estilo de silla. Básica(B) Estándar(E) De lujo(L):')
cantidad = int(input('Cantidad de sillas: '))
tipo_cliente = input('¿Qué tipo de cliente es? Frecuent(F) o Normal(N)' )
subtotal = total_antes_descuento(tipo_silla,cantidad)
print(f"Total sin dcto.  ${subtotal:>7}")
desc = descuento(subtotal,tipo_cliente)
print(f"Descuento        ${desc:>7}")
total = subtotal - desc
print(f"Total a pagar    ${total:>7}")


if __name__ == '__main__':
    main()
