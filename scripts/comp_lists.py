import numpy as np
def getMatches(a, b):
    matches = []
    unique_a = np.unique(a)
    unique_b = np.unique(b)
    for a in unique_a:
        for b in unique_b:
            if a == b:
                matches.append(a)
    return matches

def diff(list1, list2):
    c = set(list1).union(set(list2))  # or c = set(list1) | set(list2)
    d = set(list1).intersection(set(list2))  # or d = set(list1) & set(list2)
    return list(c - d)

def diff2(list1, list2):
    diff = lambda l1,l2: [x for x in l1 if x not in l2]
    return diff



print(getMatches([1, 2, 3, 4, 5], [9, 8, 7, 6, 5, 9])) # displays [5]
print(getMatches([1, 2, 3], [3, 4, 5, 1])) # displays [1, 3]
print(getMatches(["AA-1","AA-2","AA-10","BB-7"], ["AA-2","AA-1","AA-10"]))

a = ["AA-1","AA-2","AA-10","BB-7"]
b = ["AA-2","AA-1","AA-10","BB-8"]
print(diff(a, b))

print(diff(a,b))
print(diff(b,a))