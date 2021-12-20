n = int(input("Введіть кількість елементів масиву : "))
if not 0 < n <= 100:
    raise Exception("Недопустиме значення n")
a = input()
nums = list(map(lambda el: float(el), a.split(sep=" ")))
for el in nums:
    if el < 2.5:
        print("{0} {1:.2f}".format(nums.index(el)+1, el))
        break
