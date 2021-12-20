n = int(input("Введіть кількість елементів масиву : "))
if not 0<n<=100:
    raise Exception("Недопустиме значення n")
a = input()
nums = list(map(lambda el: float(el), a.split(sep=" ")))
result = list(filter(lambda el: el>0, nums))
if not len(result)==0:
    print("{0:.2f}".format(sum(result)/len(result)))
else:
    print("Not Found")