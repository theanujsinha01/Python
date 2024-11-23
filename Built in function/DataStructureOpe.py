s = "hello world"
print(s.split())  # Output: ['hello', 'world']


arr = ['hello', 'world']
print(' '.join(arr))  # Output: "hello world"


arr = [1, 2, 3]
arr.append(4)
print(arr)  # Output: [1, 2, 3, 4]


arr = [1, 2, 3]
arr.pop()
print(arr)  # Output: [1, 2]


arr = [1, 2]
arr.extend([3, 4])
print(arr)  # Output: [1, 2, 3, 4]


s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}


a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))  # Output: {1, 2, 3, 4, 5}
print(a.intersection(b))  # Output: {3}

arr = [1, 2, 3]
print(list(reversed(arr)))  # Output: [3, 2, 1]

