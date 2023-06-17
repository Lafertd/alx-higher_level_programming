#!/usr/bin/python3
def ispalindrome(n):
    number = str(n)
    return number == number[::-1]

pals = []
for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if ispalindrome(i * j):
            pals.append(i * j)
print(max(pals))
