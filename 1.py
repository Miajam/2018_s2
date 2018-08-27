
'''
Generates a list L of random nonnegative integers at most equal to a given upper bound,
of a given length, all controlled by user input.

Outputs four lists:
- elements_to_keep, consisting of L's smallest element, L's third smallest element,
  L's fifth smallest element, ...
  Hint: use sorted(), list slices, and set()
- L_1, consisting of all members of L which are part of elements_to_keep, preserving
  the original order
- L_2, consisting of the leftmost occurrences of the members of L which are part of
  elements_to_keep, preserving the original order
- L_3, consisting of the LONGEST, and in case there are more than one candidate, the
  LEFTMOST LONGEST sequence of CONSECUTIVE members of L that reduced to a set,
  is a set of integers without gaps.
'''


import sys
def judge(a): 
    e = sorted(set(a))
    if ((e[-1]) - (e[0]) +1) / len(e) == 1:
        return a[:]
    else:
        return -1

def con(L):
    j = len(L)
    while j > 0 :
        for  i in range(0, len(L)):
            if i + j <= len(L) and j >=1:
                key.append(i)
                key.append(i+j)
        j  -= 1
from random import seed, randint


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

c = []
etk = L[:]
L_0 = list(set(etk))
L_0.sort()

L_2 = []
L_3 = []

elements_to_keep = list(L_0[::2])
for i in range(0,len(L)):
    if L[i] in elements_to_keep:
        c.append(L[i])
L_1 = c[:]
L_2 = list(set(L_1))
L_2.sort(key = L_1.index)

    
key = []
con(L)
for i in range(0,len(key),2):
    if judge(L[key[i]:key[i+1]]) != -1:
        L_3 = judge(L[key[i]:key[i+1]])
        break
    else:
        continue


# Replace this comment with your code
    
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)
print('\nHere is L_1:')
print('  ', L_1)
print('\nHere is L_2:')
print('  ', L_2)
print('\nHere is L_3:')
print('  ', L_3)

