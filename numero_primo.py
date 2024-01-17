# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */
# Un número n es primo si y solo si (n-1)!  + 1 es múltiplo de n
def factorial(n):
    if n == 0 or n == 1:
        result = 1
    elif n > 1:
        result = n * factorial(n - 1)

    print(result)
    return result


def es_primo(n):
    result = True if (factorial(n - 1) + 1) % n == 0 else False
    return result


print(es_primo(4))
