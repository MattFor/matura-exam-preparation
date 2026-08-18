1. Największy Wspólny Dzielnik (GCD) [Grand Common Denominator] Euklidesa Euklides

def euclidIter(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
 
def euclidRecur(a, b):
    if a == b:
        return a
    if a > b:
        return euclidRecur(a - b, b)
    return euclidRecur(b - a, a)
 
def betterEuclidIter(a, b):
    while b != 0:
        zmienna = b
        b = a % b
        a = zmienna
    return a
 
def betterEuclidRecur(a, b):
    if a == 0:
        return b
    return betterEuclidRecur(b % a, a)
 

def gcd(a,b):
    return a if not b else gcd(b, a%b)

def gcd(a,b):
  while b:
    a,b = b, a%b
  return a

gcd = lambda a,b : a if not b else gcd(b, a%b)

2. Największa Wspólna Wielokrotność (LCM) [Least Common Multiple]

def lcm(x, y):
   greater = x if x > y else y

   while(True):
       if (greater % x == 0) and (greater % y == 0):
           lcm = greater
           break
       greater += 1

   return lcm
  
def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm
   
3. Sito Erastotenesa - Liczby Pierwsze

def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False
    p = 2
    
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
        
    return [i for i in range(n + 1) if primes[i]]

4. Ciąg Fibonacciego

def Fib(n):
    if n == 1 or n == 2:
        return 1
    return Fib(n - 1) + Fib(n - 2)
    
def Fib(n):
    a = 1
    b = 1
    for i in range(2, n):
        temp = b
        b = a + b
        a = temp
    return b
    
5. MAN 

What is a metropolitan area network (MAN)?
A metropolitan area network (MAN) is a computer network that connects 
computers within a metropolitan area, 
which could be a single large city, 
multiple cities and towns, or any given large area with multiple buildings. 
A MAN is larger than a local area network (LAN) but 
smaller than a wide area network (WAN). 
MANs do not have to be in urban areas; 
the term "metropolitan" implies the size of the network, 
not the demographics of the area that it serves.

6. LAN

A local area network (LAN) is a computer network that interconnects 
computers within a limited area such as a residence, school, laboratory, university 
campus or office building.[1] By contrast, a wide area network (WAN) not only 
covers a larger geographic distance, but also generally involves leased telecommunication circuits. 

7. Czy da się zreprezentować number w danym systemie liczbowym [Represent Number In Base]

def can_represent_in_base(number, base):
	while number > 0:
		digit = number % base
		if digit >= 2:
			return False
		number //= base
	return True

8. Matrix rotation 90deg to the right

original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rotated = [list(z) for z in zip(*original[::-1])]

9. Moda / Dominanta

from collections import Counter

lista=[1,2,3,4,5]

def moda(lista):
    if all(i == 1 for i in Counter(lista).values()):
        return lista
    return Counter(lista).most_common(1)[0][0]

def moda(lista):
    return max(set(lista), key = lista.count)

def moda2(T):
    maxi = 0
    n = len(T)
    for i in range(n):
        count = 0
        for j in range(n):
            if T[i] == T[j]:
                count += 1
        if count > maxi:
            maxi = count
            moda = T[i]
    return moda

10. Mediana

def mediana(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j + 1], lista[j] = lista[j], lista[j + 1]

    if len(lista) % 2 == 0:
        mediana = lista[int(len(lista) / 2)] + lista[int(len(lista) / 2 - 1)]
        mediana /= 2
    else:
        mediana = lista[int(len(lista) / 2)]
    return mediana