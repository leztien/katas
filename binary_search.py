"""
binary search
"""

from random import randint


def make_search_space(n, max_value=None):
    max_value = int(max_value or n*2)
    return tuple(sorted(randint(0, max_value) for _ in range(n)))
    
  
def binarysearch(seq, item):
    lo, hi = 0, len(seq) - 1
    
    while not (lo > hi):
        ix = (lo + hi) // 2
        curr = seq[ix]
        
        if item < curr:
            hi = ix - 1
        elif item > curr:
            lo = ix + 1
        else: # item == curr
            return ix
    return 'not found'
