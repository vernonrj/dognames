"""Create random dog names"""
import random
from functools import reduce

from dog_list import DOGS


def word_iter(words):
    """iterate on words"""
    word = []
    for char in words:
        if char in ' \n\t':
            if word:
                yield ''.join(word)
                word = []
        else:
            word.append(char)


def rand_elem(indexable):
    """return an element at random from an indexable collection"""
    elem = random.randint(0, len(indexable) - 1)
    return indexable[elem]

def hyphenate(phrase):
    """hyphenate a phrase correctly"""
    return reduce(list.__add__, (x.split('-') for x in phrase.split()))

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
