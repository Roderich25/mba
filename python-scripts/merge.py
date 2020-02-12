#!/usr/bin/env python3
a = [i*2+1 for i in range(0, 5)]
b = [i+3 for i in range(1, 8)]
c = []
i = 0
j = 0


while i < len(a) or j < len(b):
    menor = 999
    if i < len(a) and a[i] < menor:
        menor = a[i]
        cual = 1
    if j < len(b) and b[j] < menor:
        menor = b[j]
        cual = 2
    if cual == 1:
        i += 1
    if cual == 2:
        j += 1
    c.append(menor)
print(a)
print(b)
print(c)
