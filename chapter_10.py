# Lists
[23,614, 32, 54]
['spam', 32, 43.21, [2,3]]

# List are mutable
# The in operator alsa works on lists
a = [23, 134, 621, 1,23]
23 in a # True
24 in a # False

numbers = [3, 12, 1, 31,32]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

[4] * 3 #[4, 4, 4]


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
#[1, 2, 3, 4, 5, 6]


# Slice a list with
a[2:3]
a.append(63)

# Extend takes a list as an argument
t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
#['a', 'b', 'c', 'd', 'e']

###### Methods modify the list
sum(a)

# A variable used for accumulate the sum of the variables is sometimes called accumulator

# An operator like this that combines a sequence of values into a single value is sometimes called reduce

# A map is sometimes called this way because it 'maps' a function onto each of the elements of a sequence

# A filter is when a function selects some of the elements and filter out the rest

# Deleting elements
t = ['a','b','c','d']
t.pop(1)
del t[1]
# Or with the remove method
t.remove('a')

if 'd' in t:
    t.remove('d')

x = 'hello'
saludo = list(x)

s = 'The sun has got his hat on'
# Default delimiter is space
delimiter = ' '
t = s.split()
t1 = s.split(delimiter)

# Join is the inverse of split

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t)
#'pining for the fjords'

a = 'banana'
b = 'banana'
a is b
#True

a = [1, 2, 3]
b = [1, 2, 3]
a is b
#False
# Identical and equivalent

# When you pass a list to a function it is passed by reference so it can affect the original values
# There are operations that modify a list and others that create a new list

#####DEBUG
t = [43,3,12,8]
x = [32,78,9]

word = 'Hola mundo'
word = word.strip()
#list
#t = t.sort() # WRONG!

t.append(x)
t = t + [x]
t += [x]


#t.append([x]) # WRONG!
#t = t.append(x) # WRONG!
#t + [x] # WRONG!
#t = t + x # WRONG!

#Make a copy
t = [1, 2, 3]
t2 = t[:]
t2.sort
#or use
t2 = sorted(t)

