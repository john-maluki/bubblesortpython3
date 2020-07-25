def bs(a):
    b = len(a) - 1
    for x in range(b):
        for y in range(b - x):
            if a[y] > a[y + 1]:
                a[y], a[y + 1] = a[y + 1], a[y]
                
    return a

import random
mylist = []
for i in range(0,10):
    n = random.randint(1,100)
    mylist.append(n)

bs(mylist)
print('The sorted list is: ')
print(mylist)
