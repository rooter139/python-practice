eng2sp = dict()

eng2sp['one'] = 'uno'
print(eng2sp['one'])

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

#length
len(eng2sp)
print('one' in eng2sp) #True
print('uno' in eng2sp) #False

vals = eng2sp.values()
'uno' in vals # True

####
#An implementation is a way performing computation


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

h = {'a' : 1}
#32 is just a default value it could be any value
h.get('a',32)
#1
h.get('c',32)
#32
h.get('c',"valor por default")
#32

def print_hist(h):
    for c in h:
        print(c, h[c])


def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

# The raise statement causes an exception
#raise LookupError('value does not appear in the dictionary')


#memos
#A previously computed value that is store for later use is called memo


known = {0:0, 1:1}
def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

#Valiables declared outside a function are in __main__ they are global
been_called = False

def example2():
    global been_called
    been_called = True

#exception when the global variable refers to a mutable value you can modify the value without declaring the variable
known = {0:0, 1:1}
def example4():
    known[2] = 1

#pprint stands for “pretty print”)