"""
bubble sort
"""

from random import randint

def make_seq(n, max_value=None):
    max_value = int(max_value or n*2)
    return [randint(0, max_value) for _ in range(n)]


def bubblesort(l):
    sorted = False
    while not sorted:
        sorted = True  # assume l is sorted
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                sorted = False
