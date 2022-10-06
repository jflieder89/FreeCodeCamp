"""
Return the number of total permutations of the provided string that don't have repeated consecutive letters.
Assume that all characters in the provided string are each unique.
For example, aab should return 2 because it has 6 total permutations (aab, aab, aba, aba, baa, baa),
but only 2 of them (aba and aba) don't have the same letter (in this case a) repeating.
"""
from itertools import permutations
def permAlone(item):
    perms = [''.join(p) for p in permutations(item)]
    final_lst = [] #list to be filled with acceptable permutations
    for perm in perms:
        flag = False #flag to see if consecutive characters are a repeat. flag to be set to True if that is found for a permutation
        for i in range(len(item) - 1):
            if perm[i] == perm[i+1]:
                flag = True
        if flag == False:
            final_lst.append(perm)
    return len(final_lst)

print(permAlone('aaabb'))
