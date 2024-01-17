# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */

def is_anagram(word1, word2):
    first = word1.lower()
    second = word2.lower()[::-1]
    result = True if first == second else False
    return result


def main():
    print("Ingrese la primera palabra")
    first = input()
    print("Ingrese la segunda palabra")
    second = input()
    print(f'Las palabras proporcionadas corresponden a un Anagrama?: {is_anagram(first, second)}')


main()


