n = int(input("Введіть кількість елементів масиву : "))
if not 0 < n <= 101:
    raise Exception("Недопустиме значення n")
a = input()
nums = list(map(lambda el: int(el), a.split(sep=" ")))
len_nums = len(nums)
if len_nums == n:
    for i in range(abs(min(nums)), 0, -1):
        j = 0
        while j < len_nums:
            if nums[j] % i == 0:
                j += 1
            else:
                break
        if j == len_nums:
            result = i
            break
else:
    print("Невірна кількість елементів")
print(result)