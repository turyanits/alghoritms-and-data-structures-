n = int(input("Введіть кількість елементів масиву : "))
if not 0 < n <= 100:
    raise Exception("Недопустиме значення n")
a = input()
nums = list(map(lambda el: float(el), a.split(sep=" ")))
if len(a) > n:
    print("Невірна кількість елементів")
print("{0:.2f}".format(abs(max(nums, key=abs))))
