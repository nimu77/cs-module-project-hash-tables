"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

sums = {}

diffs = {}

for i in q:
    for x in q:
        s = f(i) + f(x)
        if s in sums:
            sums[s].append((i, x))
        else:
            sums[s] = [(i, x)]
            
        d = f(i) - f(x)
        if d in diffs:
            diffs[d].append((i, x))
        else:
            diffs[d] = [(i, x)]
            
for key in sums:
    if key in diffs:
        for value in sums[key]:
            for dvalue in diffs[key]:
                A, B, C, D = value[0], value[1], dvalue[0], dvalue[1]
                assert(f(A) + f(B) == f(C) - f(D))
                print(f'f({A}) + f({B}) = f({C}) - f({D})'
                      f'    {f(A)} + {f(B)} = {f(C)} - {f(D)}')
