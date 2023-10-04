#lambda - can take any number of arguements

x = lambda a,b : a + b
print(x(5,6))

y = lambda a,b : a + " " + b
print(x("you","are"))

def myfunc(n):
    return lambda a : a*a*n
mydoubler = myfunc(2)
print(mydoubler(11))
