import math
n = int(input('n: '))
numb = list(map(int, input().split(' ')))

if len(numb) != n:
    raise Exception("Хибне значення n")

if n % 2 != 0:
    numb.insert(0, numb.pop(math.floor(n/2)-1))
    numb.insert(-1, numb.pop(math.ceil(n/2)+1))
else:
    numb.insert(0, numb.pop(int(n/2)-1))
    numb.insert(n-1, numb.pop(int(n/2)))


print(*numb)