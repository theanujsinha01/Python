arr = [5, 3, 8, 1]
print(sorted(arr))  # Output: [1, 3, 5, 8]



arr = [5, 3, 8, 1]
arr.sort()
print(arr)  # Output: [1, 3, 5, 8]


arr = [5, 3, 8, 1]
print(min(arr))  # Output: 1
print(max(arr))  # Output: 8


arr = [5, 3, 8, 1]
print(arr.index(8))  # Output: 2


nums = [1, 2, 3]
print(list(map(lambda x: x * 2, nums)))  # Output: [2, 4, 6]


nums = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, nums)))  # Output: [2, 4]
