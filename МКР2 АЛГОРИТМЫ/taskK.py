a = input("Введіть n, a, b, c, d: \n")
nums = list(map(lambda el: int(el), a.split(sep=" ")))
if len(nums) != 5 or nums[1] > nums[2] or nums[3] > nums[4]:
    raise Exception("Значення недопустимі")
b = [i for i in range(1, nums[0]+1)]

print(b[:nums[1]-1:]
      + list(reversed(b[nums[1]-1:nums[2]:]))
      + b[nums[2]:nums[3]-1:]
      + list(reversed(b[nums[3]-1:nums[4]:]))
      + b[nums[4]::])
