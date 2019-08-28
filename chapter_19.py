## Conditional expressions
import math
if x > 0:
    y = math.log(x)
else:
    y = float('nan')

y = math.log(x) if x > 0 else float('nan')


## List comprehensions
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

#We can write this more concisely using a list comprehension:
def capitalize_all(t):
    return [s.capitalize() for s in t]

## Generator expressions
g = (x**2 for x in range(5))

next(g)
next(g)
#...
for val in g:
    print(val)

# If we reach the last value it raises an exception
next(g)
#StopIteration

sum(x**2 for x in range(5))

## any and all
#any takes a sequence of boolean values and returns True if any of the values are True
any([False, False, True])
#True

#It is often used with generator expressions
any(letter == 't' for letter in 'monty')
#True

#all returns True if every element of the sequence is True

## Set
def subtract(d1, d2):
    return set(d1) - set(d2)

def has_duplicates(t):
    return len(set(t)) < len(t)

## Counters
from collections import Counter
count = Counter('parrot')
count
#Counter({'r': 2, 't': 1, 'o': 1, 'p': 1, 'a': 1})

def is_anagram(word1, word2):
    return Counter(word1) == Counter(word2)

## defaultdict
from collections import defaultdict
d = defaultdict(list)

t = d['new key']
t
#[]

t.append('new value')
d
#defaultdict(<class 'list'>, {'new key': ['new value']})

## Named tuples
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p
#Point(x=1, y=2)

## Gathering keyword args

# To gather keyword arguments, you can use the **operator
def printall(*args, **kwargs):
    print(args, kwargs)

