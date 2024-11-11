#break
number = [1,2,3,4,5]
for i in number:
    if i == 3:
        break
    print(i)

#continue -- skip
for i in number:
    if i==3:
        continue
    print(i)

# pass : Do nothing when ith iteration condtion
for i in range(5):
    if i==2:
        pass 
    print(i)
