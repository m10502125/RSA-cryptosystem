
from math import sqrt
import secrets
import cProfile
import re
import fractions
import sys
sys.setrecursionlimit(10000)
def ext_euclid(e,n):
    if(n==0):
        return 1,0,e
    else:
        x,y,q = ext_euclid(n,e%n)
        x,y = y, (x-(e//n)*y)
        return x,y,q
def fermat_isPrime(num):
    if num ==2 :
        return True
    if not num & 1:
        return False
    return pow(2,num-1,num) == 1

def next_prime(num):
    # If num is an even number
    # let num be an odd number by adding 1
    if (num!=2) and (num%2==0):
        num+=1
    if fermat_isPrime(num):
        num = num + 2
    while True:
        if fermat_isPrime(num):
            break
        num = num +2
    return num

num1 = secrets.randbits(1024)
prime1 = next_prime(num1)
#print(prime1,"is a prime")
num2 = secrets.randbelow(2**1025-1)
prime2 = next_prime(num2)
#print(prime2,"is a prime")
N = prime1*prime2
print("N:",N)
#print("diff:",prime1-prime2)
phi_N = (prime1-1) * (prime2-1)
#print("phi_N",phi_N)
e = secrets.randbelow(2**20)
while True:
    if fractions.gcd(e,phi_N) == 1:
        print("e:",e)
        break
    e = secrets.randbelow(2**20)
# ex + by = q
d,y,gcd = ext_euclid(e,phi_N)
if d<0:
    d = d + phi_N
print("d:",d)

m = 94
C=pow(m,e,N)
m2 = pow(C,d,N)
print("m: ",m,", m2: ",m2)

f = open('RSA_Keys','w')

f.write('\np is ')
s = str(prime1)
f.write(s)

f.write('\nq is ')
s = str(prime2)
f.write(s)

f.write('\nN is ')
s = str(N)
f.write(s)

f.write('\nphi_N is ')
s = str(phi_N)
f.write(s)

f.write('\ne is ')
s = str(e)
f.write(s)

f.write('\nd is ')
s = str(d)
f.write(s)

f.write('\nC is ')
s = str(C)
f.write(s)
