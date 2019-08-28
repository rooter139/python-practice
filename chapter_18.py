#Inheritance
class Deck:
    """Muestra """

class Hand(Deck):
    """Represente a hand of playing cards."""


def find_defining_class(obj, meth_name):
    for ty in type(obj).mro():
        if meth_name in ty.__dict__:
            return ty

#This example suggests a development plan for designing objects and methods:
#1. Start by writing functions that read and write global variables (when necessary).
#2. Once you get the program working, look for associations between global variables
# and the functions that use them.
#3. Encapsulate related variables as attributes of an object.
#4. Transform the associated functions into methods of the new class.