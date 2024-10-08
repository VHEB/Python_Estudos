from itertools import count

c1 = count()
r1 = range(10)

print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('Count')
for i in c1:
    print(i)
    if i == 10:
        break
    #Se não colocar o break, ele vai continuar infinitamente
    #Cuidado para não travar o computador