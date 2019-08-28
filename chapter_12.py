#tuples
#tuples are IMMUTABLE

t = ('a', 'b', 'c', 'd', 'e')

t[0]
t[0:2]

#To create a tuple with a single element, you have to include a final comma:
t1 = 'a',
type(t1) # tuple
###A value in parentheses is not a tuple:
t2 = ('a') #<class 'str'>


t = tuple()


t
#('h', 'o', 'l', 'a')
t = t[0:3] + ('A',)
t
#('h', 'o', 'l', 'A')


temp = t
t = t1
t1 = temp

t, t1 = t1, t

#Strictly speaking, a function can only return one value, but if the value is a tuple, the effect
#is the same as returning multiple values

#A function can return multiple values
t = divmod(7, 3)
t
#(2, 1)

#gather
def printall(*args):
    print(args)
#scatter
divmod(*t)

#A zip takes two or more sequences and interleaves them
s = 'abc'
t = [0, 1, 2]
zip(s, t)
for pair in zip(s, t):
    print(pair)

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print(number, letter)

for index, element in enumerate('abc'):
    print(index, element)

t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)

d = dict(zip('abc', range(3)))
d
#{'a': 0, 'c': 2, 'b': 1}


directory = dict()
directory['Monroy', 'Daniel'] = '552343'
directory['Irineo', 'Oscar'] = '626772'
directory
#{('Monroy', 'Daniel'): '552343', ('Irineo', 'Oscar'): '626772'}

#http://thinkpython2.com/code/structshape.py

######13

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))
        t.sort(reverse=True)
    return t

def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, freq, sep='\t')
#The first parameter is required; the second is optional. The default value of num is 10.

