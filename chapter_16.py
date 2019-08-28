#Pure functions

#there are two models 
#prototype and patch
#planning called designed development


def add_time(t1, t2):
#    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

#This is called a pure function because it does not modify any of the objects
#passed to it as arguments and it has no effect, like displaying a value or getting user input,
#other than returning a value.

#Modifiers

#Sometimes it is useful for a function to modify the objects it gets as parameters. In that case,
#the changes are visible to the caller. Functions that work this way are called modifiers.


#invariant: A condition that should always be true during the execution of a program.