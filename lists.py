from functools import reduce

nums = [1, 2, 3, 4, 5]
print(nums)

# Map
doubled = list(map(lambda x: x * 2, nums))
print(doubled)

# Filter
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Reduce
total = reduce(lambda x, y: x + y, nums)
print(total)
