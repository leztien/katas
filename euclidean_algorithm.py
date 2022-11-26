"""
euclidean algorithms (iterative)
"""


from random import randint


def generate():
    a,b = sorted((randint(2,100) for _ in range(2)), reverse=True)
    if randint(0,1): return a,b
    d = randint(1,50)
    m,n = (randint(2,15) for _ in range(2))
    a,b = sorted((d*k for k in (m,n)), reverse=True)
    return a,b


##################################################################

a,b = generate()


def gcd(a,b):
    while a != b:
        c = a - b
        a,b = (b,c) if b>c else (c,b)    
    return a


d = gcd(a, b)
print((a,b), d)
