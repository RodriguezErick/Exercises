# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */

def area(i):
    if i == 1:
        base = int(input("Ingrese en numero la medida de la base: "))
        alt = int(input("Ingrese en numero la medida de la altura: "))
        result = (base * alt) / 2
        print(f'El area del triangulo es: {result}')
        return main()

    elif i == 2:
        lado = int(input("Ingrese en numero la medida de un lado: "))
        result = lado * lado
        print(f'El area del cuadrado es: {result}')
        return main()

    elif i == 3:
        base = int(input("Ingrese en numero la medida de la base: "))
        alt = int(input("Ingrese en numero la medida de la altura"))
        result = base * alt
        print(f'El area del rectangulo es: {result}')
        return main()


def main():
    print("Ingrese el numero de la opcion elegida")
    print("1. Triangulo")
    print("2. Cuadrado")
    print("3. Rectangulo")
    print("4. Salir")
    a = int(input())
    area(a)


main()

