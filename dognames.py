"""Create random dog names"""
import hyphen
import random
from functools import reduce

H_EN = hyphen.Hyphenator()

DOGS = \
"""
Afghan Hound
Basset Hound
Beagle
Border Collie
Boston Terrier
Bulldog
Bullmastiff
Chihuahua
Cocker Spaniel
Dachsund
Deerhound
Dobermann
Fox Terrier
German Shepherd
Golden Retriever
Great Dane
Greyhound
Harrier
Husky
Irish Setter
Labradoodle
Labrador Retriever
Maltese
Pit Bull
Poodle
Saint Bernard
Shitzu
Teacup Poodle
"""

def rand_elem(indexable):
    """return an element at random from an indexable collection"""
    elem = random.randint(0, len(indexable) - 1)
    return indexable[elem]

def hyphenate(phrase):
    """hyphenate a phrase correctly"""
    try:
        return reduce(list.__add__, (H_EN.syllables(x) for x in phrase.split()))
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
