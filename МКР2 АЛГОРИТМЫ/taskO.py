n = int(input('N: '))
a = list(map(int, input('Введіть числа першого масиву : ').split(' ')))

if len(a) != n:
    raise Exception("Недопустиме значення N")

m = int(input('M: '))
b = list(map(int, input('Введіть числа другого масиву : ').split(' ')))
if len(b) != m:
    raise Exception("Недопустиме значення M")

result = []
for el in a:
    if el not in b:
        result.append(el)

print(len(result))
print(*result)