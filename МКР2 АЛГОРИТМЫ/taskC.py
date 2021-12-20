n = int(input("Введіть кількість елементів масиву : "))
if not 0 < n <= 100:
    raise Exception("Недопустиме значення n")
a = input()
nums = list(map(lambda el: int(el), a.split(sep=" ")))
result = list(filter(lambda el: el % 6 == 0, nums))
print(len(result), sum(result))
