# /*
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */
# Fn = Fn-1 + Fn-2.

def fibonacci():
    lista = []
    for i in range(51):
        if i - 2 < 0:
            lista.append(i)
        else:
            lista.append(lista[i-1] + lista[i - 2])
    return print(lista)


fibonacci()

