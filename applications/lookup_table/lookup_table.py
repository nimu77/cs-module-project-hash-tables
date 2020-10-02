# Your code here
import random
import math

def slowfun_too_slow(x, y):
    # x =4
    # y=3
    # breakpoint()
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    
    
    return v

# value_v = {}

# def lookup_table():
#     for i in range(1, 1000):
#         value_v[i] = math

cache = {}
def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # check if the key x and y is does not exist in the cache
        # call the function above
    if (x, y) not in cache:
        cache[(x, y)] = slowfun_too_slow(x, y)

    return cache[(x, y)]







# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

# print(slowfun_too_slow(2, 4))
