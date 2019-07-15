#from functool import reduce

def christy(n):
    return lambda a : a * n
a = christy(2)
b = christy(3)

print(a(12))
print(b(11))