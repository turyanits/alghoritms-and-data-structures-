a = input()
nums = list(map(lambda el: int(el), a.split(sep=" ")))
result = 0
for i in range(10):
    result += nums.count(i)//2
print(result)