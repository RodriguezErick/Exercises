
# /* FIZZBUZZ
#  * Escribe un programa que muestre por consola (con un print) los
#  * números de 1 a 100 (ambos incluidos y con un salto de línea entre
#  * cada impresión), sustituyendo los siguientes:
#  * - Múltiplos de 3 por la palabra "fizz".
#  * - Múltiplos de 5 por la palabra "buzz".
#  * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#  */

def is3multiple(n):
    is_multiple = True if n % 3 == 0 else False
    return is_multiple


def is5multiple(n):
    is_multiple = True if n % 5 == 0 else False
    return is_multiple


def is3_5multiple(n):
    is_multiple = True if is3multiple(n) is True & is5multiple(n) is True else False
    return is_multiple


def print_number(list_number):
    for n in list_number:
        if is3_5multiple(n):
            n = "fizzbuzz"
        elif is5multiple(n):
            n = "buzz"
        elif is3multiple(n):
            n = "fizz"

        print(n)
    return ""


def main():
    numbers = list(range(1, 100 + 1))
    print(print_number(numbers))


main()

