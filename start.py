print("Hello world")
print("bye")
print(type(2))
#we execute these to identify the results of the variables
print(5)
x=5
print(x+1)
import math
print(math.pi)

#When you create a variable outside of any function, it belongs to __main__
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

### justify a string at 70
def right_justify(s):
    print(" "*(70-len(s))+ s)

right_justify("monty")

#
def do_twice(f,cadena):
    f(cadena)
    f(cadena)

def print_spam(valor):
    print(valor)

do_twice(print_spam,"Spam")