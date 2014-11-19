"""Create random dog names"""
import random
from functools import reduce


DOGS = \
"""
Af-ghan Hound
Bass-et Hound
Bea-gle
Bor-der Col-lie
Bost-on Ter-ri-er
Bul-ldog
Bull-mas-tiff
Chi-hua-hua
Cock-er Span-iel
Dach-sund
Deer-hound
Do-ber-mann
Fox Ter-ri-er
Ger-man Shep-herd
Gol-den Re-triev-er
Great Dane
Grey-hound
Har-ri-er
Hus-ky
I-rish Set-ter
Lab-ra-doo-dle
Lab-ra-dor Re-triev-er
Mal-tese
Pit Bull
Poo-dle
Saint Ber-nard
Shi-tzu
Tea-cup Poo-dle
"""

def rand_elem(indexable):
    """return an element at random from an indexable collection"""
    elem = random.randint(0, len(indexable) - 1)
    return indexable[elem]

def hyphenate(phrase):
    """hyphenate a phrase correctly"""
    try:
        return reduce(list.__add__, (x.split('-') for x in phrase.split()))
    except IndexError:
        return []

def mangle_dog_names(names):
    """return all those names mangled up"""
    sylls = (hyphenate(x) for x in names.strip().splitlines())
    return list(set(reduce(list.__add__, sylls)))

SYLLABLES = mangle_dog_names(DOGS)


def create_dog_name():
    """create a random dog name"""
    num_syllables = random.randint(2, 4)
    name = ''.join((rand_elem(SYLLABLES) for _ in range(num_syllables)))
    return name.lower().capitalize()


if __name__ == '__main__':
    print(create_dog_name())
