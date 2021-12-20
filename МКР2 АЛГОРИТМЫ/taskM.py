n = int(input("Введіть кількість елементів масиву : "))
if not 1 < n <= 100:
    raise Exception("Недопустиме значення n")
a = input()
nums = list(map(lambda el:int(el), a.split(sep=" ")))
count = saved_count = 0
if len(nums) == n:
    for el in nums:
        if el > 0:
            count += 1
        else:
            count = 0
        if count > saved_count:
            saved_count = count
print (saved_count)