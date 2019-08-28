# By convention the first parameter of a method is called self

# inside class Time:
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

# The __init__ method short for initialization is a special method that gets invoked when an object is instanciated

# inside class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

# The __str__ method is a special method, that it is supposed to return a string representation of an object
# inside class Time:
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

# When you print an object, Python invokes the str method:
time = Time(9, 45)
print(time)
#09:45:00

# When I write a new class, I almost always start by writing __init__, which makes it easier to instantiate objects, and __str__, which is useful for debugging.

# Operator overloading
#By defining other special methods, you can specify the behavior of operators on
#programmer-defined types. For example, if you define a method named __add__ for the
#Time class, you can use the + operator on Time objects.

# inside class Time:
    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

#isinstance takes a value and a class object
# it is used in an operation called type-based dispatch

#For purposes of debugging, you might find it useful to keep this function handy:
def print_attributes(obj):
    for attr in vars(obj):
        print(attr, getattr(obj, attr))