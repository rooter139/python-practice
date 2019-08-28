#import copy
#p2 = copy.copy(p1)

#box2 = copy.copy(box)
#box2 is box
#False
#box2.corner is box.corner

#box3 = copy.deepcopy(box)
#box3 is box
#False
#box3.corner is box.corner
#False

#type(p)
#<class '__main__.Point'>
#You can also use isinstance to check whether an object is an instance of a class:
#isinstance(p, Point)
#True

#hasattr(p, 'x')

#try:
#x = p.x
#except AttributeError:
#x = 0

