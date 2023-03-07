from collections import deque
from copy import deepcopy

lines = open("25.in").read().strip().split("\n")
# lines = open("example.in").read().strip().split('\n')

SNAFU =[] 
for line in lines:
    SNAFU.append(line.strip())

to_dec = { '2': 2, '1': 1, '0': 0, '-': -1, '=': -2 }
D  = []
while SNAFU:
    n = SNAFU.pop()
    p = 1
    dec = to_dec[n[-1]]
    for nn in range(len(n) - 2, -1, -1):
        p *= 5
        dec += (to_dec[n[nn]] * p)
    D.append(dec) 

print(sum(D))

add_to_fiv = {
    (0, '0'): '0',
    (0, '1'): '1',
    (1, '0'): '1',
    (1, '1'): '2',
    (2, '0'): '2',
    (2, '1'): '1=',
    (3, '0'): '1=',
    (3, '1'): '1-',
    (4, '0'): '1-',
    (4, '1'): '10',
}

to_fiv = { 0: '0', 1: '1', 2: '2', 3: '1=', 4: '1-' }
q = sum(D)
fiv = ''
c = 1
while True:
    q, r = q // 5, q % 5

    if len(fiv) == c:
        fiv = add_to_fiv[(r, fiv[0])] + fiv[1:]
    else :
        fiv = to_fiv[r]  + fiv
        
    c += 1
    if q == 0:
        break
print(fiv)
