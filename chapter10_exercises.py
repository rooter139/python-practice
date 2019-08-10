def nested_sum (t):
    sum = 0
    for element in t:
        for iElement in element:
            sum += iElement
    return sum
        

t = [[1, 2], [3], [4, 5, 6]]
x = nested_sum(t)
print(x)

#t.__len__()

def cumsum(t):
    accumulator = 0
    for el in t:
        accumulator += el
    t2 = t[0: len(t) -1]
    t2.append(accumulator)
    return t2

t = [1, 2, 3]
t2 = cumsum(t)
print(t2)




