"""
Given a number N, find all factors of N.

Example:

N = 6 
factors = {1, 2, 3, 6}
Make sure the returned array is sorted.

"""
# This is the first approach and this approach take too much time for problem solving.
# This is take 27 secs 

def allFactors(A):
    L = []
    i = 1
    while i<A:
        if A%i==0:
            L.append(A)
        
        i += 1

    if A not in L:
        L.append(A)

    return L



# This is second Approach and this approach take less than first 
# This is take 13 secs

def allFactors(A):
    L = []
    s = int(A//2)+1
    for i in range(1, s):
        if A%i==0:
            L.append(i)

    if A not in L:
        L.append(A)

    return L


# This is third Approach and this approach much less time and most time efficient approach
# This Approach take 80-90 milli secs

import math

def allFactors(A):
    l = []
    s = int(math.sqrt(A)+1)
    for i in range(1, s):
        if A%i==0:
            l.append(i)

    for j in l[::-1]:
        d = int(A//j)
        if d not in l:
            l.append(d)

    return l


print(allFactors(238003232))