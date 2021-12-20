n = int(input("Введіть кількість елементів масиву : "))
if not 0 < n <= 100:
    raise Exception("Недопустиме значення n")
result = ""
a = input()
nums = list(map(lambda el:int(el), a.split(sep=" ")))
if len(nums) == n:
    for el in nums:
        if el >= 0:
            el += 2
        result += str(el) + " "
else:
    print("Невірна кількість елементів")
print(result)