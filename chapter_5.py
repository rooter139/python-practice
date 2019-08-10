#Floor division operator //
print(105/60)
print(105//60)

#modulus operator
remainder = 45 % 60
print(remainder)
# True boolean
print(5 == 5)
#do nothing
if remainder > 45 and remainder < 60:
    pass
elif remainder <= 45:
    print("Menor o igual de 45")
else:
    print("Mayor de 60")

#Concise option
if 45 < remainder < 60:
    pass
#If a function calls itself it is called recursive
#text = input('Hello Mr ...')
#We have to be careful with spaces and tabs
import time
print(time.time())
