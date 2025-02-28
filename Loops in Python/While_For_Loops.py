count = 1
while count <= 5:
    print(count) # Output: 1, 2, 3, 4, 5
    count += 1


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

i = 0
while i < len(nums):
    print(nums[i])  # Output: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
    i += 1

x = 36
idx = 0

while idx < len(nums):
    if nums[idx] == x:
        print(f'Found {x} at index {idx}')  # Output: Found 36 at index 5
    idx += 1

# Break and Continue statements
count = 0
while(count < 5):
    print(count) 
    count += 1
    if(count == 3): # Output: 0, 1, 2
        break


count = 0
while(count < 5):
    count += 1
    if(count == 3):
        continue
    print(count) # Output: 1, 2, 4, 5

# For loop
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in nums:
    print(num)  # Output: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100

for i in range(0,len(nums)):
    print(nums[i])  # Output: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100


for i in range(0, 10, 2):
    print(i)  # Output: 0, 2, 4, 6, 8


# Pass statement
for i in range(0, 10, 2):
    pass # Output: No output





