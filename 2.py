
'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
sys.setrecursionlimit(1000000)
from math import gcd



try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
	
    


    

has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''

global L_s
global L_y
L_s=[]
L_y=[]
sig=[]
ta=[]


def zhi(n):
    if n==1:
        return True
    if n%2==0:
        return zhi(n//2)
    if n%5==0:
        return zhi(n//5)
    return False
def simp (m,n):
    if m>=n:
        m= m-n
        return simp(m,n)
    else:
        return (m,n)
def acc(a,b):
    z = a
    m = b
    global s
    z *= 10
    if m > z:
        L_s.append(0)
        return acc(z,m)
    else:
        s = z // m
        if z in L_y:
            return s
        else:
            L_s.append(s)
            L_y.append(z)
            return acc(z % m,m)
def to_str(L):
    for i in range(len(L)):
        L[i]=str(L[i])
    return L
def fin(a,b,s):
    if a==0:
        return 1
    else:
        s.append(a*10//b)
        fin(a*10%b,b,s)

if zhi(denominator//gcd(numerator,denominator)):
    has_finite_expansion = 1
integral_part= numerator//denominator
if not has_finite_expansion:
    simp(numerator, denominator)
    ac = acc(numerator, denominator)

    sig.extend(L_s[0:L_s.index(ac)])
    sig=to_str(sig)
    sigma=''.join(sig)
    
    ta.extend(L_s[L_s.index(ac):])
    ta=to_str(ta)
    tau=''.join(ta)
else:
    if numerator%denominator==0:
        pass
    else:
        s=[]
        fin(numerator-integral_part*denominator, denominator,s)
        s=to_str(s)
        sigma=''.join(s)

# Replace this comment with your code

if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator} / {denominator} = {integral_part}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
else:
    print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')

