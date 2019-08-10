#traversal pattern
fruit = 'banana'
index = 0 
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

for letter in fruit:
    print(letter)

def reverse_string(cadena):
    index = len(cadena)
    while index > 0 :
        print(cadena[index-1])
        index = index -1

reverse_string('pagara')

#slice string
fruit = 'banana'
s = 'Monty Python'
print(s[0:5] + fruit[:3])

#Search is a pattern of computation that traverse a sequence and return what we are looking for


def is_palindromo(cadena):
    tmp_cadena = cadena.lower().replace(' ','')
    index = 0
    last_index = len(tmp_cadena) -1
    while index <= last_index:
        if tmp_cadena[index] != tmp_cadena[last_index]:
            print('No es palindromo')
            return
        index =  index + 1
        last_index = last_index -1
    print('Es un palindromo')

is_palindromo('Able was I ere I saw Elba')
is_palindromo('Madam Im Adam')
        
#String methods
word = 'banana'
new_word = word.upper()
index = word.find('a')
word.find('na',3)
'a' in 'banana'


def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2)-1
    while j >= 0:
        print(i, j) # print here
        if word1[i] != word2[j]:
            return False
        i = i+1
        j = j-1
    return True

print(is_reverse('pots', 'stop'))