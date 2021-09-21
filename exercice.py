
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    tout_les_noms = []
    for i in range(len(prefixes)):
        tout_les_noms.append(prefixes[i] + suffixe)
    return tout_les_noms


def prime_integer_summation() -> int:
    nb_seen = 2
    prime_nb_seen = 0
    sum_of_prime = 0
    prime_seen = []
    while prime_nb_seen < 100:
        prime_nb = True
        for i in range(len(prime_seen)):
            if prime_seen[i] <= math.sqrt(nb_seen) and nb_seen % prime_seen[i] == 0:
                    prime_nb = False
                    break
            else:
                break

        if prime_nb:
            prime_seen.append(nb_seen)
            prime_nb_seen += 1
            sum_of_prime += nb_seen
        nb_seen += 1
    return sum_of_prime


def factorial(number: int) -> int:
    rep = 1
    for i in range(1, number + 1):
        rep *= i
    return rep


def use_continue() -> None:
    rep = ""
    for i in range(1, 11):
        if i != 5:
            rep += " " + str(i)
        else:
            continue
    return rep


def verify_ages(groups: List[List[int]]) -> List[bool]:
    rep=[]

    for i in range(len(groups)):
        Vrai=True
        print(len(groups[i]))
        if len(groups[i]) > 10 or len(groups[i]) < 3:
            rep.append(False)
            Vrai=False
            print("False taille",i)
        else:
            for j in range(len(groups[i])):
                if groups[i][j] < 18 and 25 not in groups[i]:
                    rep.append(False)
                    Vrai=False
                    print("False mineur",i)
                    break
                elif groups[i][j] > 70 and 50 in groups[i] and 25 not in groups[i]:
                    rep.append(False)
                    Vrai=False
                    print("False 70 et 50",i)
                    break
        if Vrai:
            rep.append(True)
    return rep


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")

    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
        [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
        [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()

print(prime_integer_summation())