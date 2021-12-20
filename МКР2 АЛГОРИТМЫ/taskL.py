n = int(input("Введіть кількість товару для 1-го магазину "))
a = list(map(int, input().split(sep=" ")))
if not len(a) == n:
    raise Exception("Недопустима довжина цін товарів для 1-го магазину")
m = int(input("Введіть кількість товару для 2го магазину "))
b = list(map(int, input().split(sep=" ")))
if not len(b) == m:
    raise Exception("Недопустима довжина цін товарів для 1-го магазину")
c = a + b
c = set(c)
print(sorted(list(c)))