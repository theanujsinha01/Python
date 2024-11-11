# Dictionary : it is used to store key : value pair
mydict = {'ramesh':1, 'mohit':2, 'hitesh':10}
print(mydict)

#access value using key
ans = mydict['mohit']
print(ans)

#key() and values() function
x = mydict.keys()
y = mydict.values()
print(x)
print(y)

#length of dictionary
print(len(mydict))

#change the value of dict
mydict['mohit'] = 20
print(mydict['mohit'])

#add value to dict
mydict['pankaj'] = 50
print(mydict)

#remove item from dict
#using pop()
mydict.pop('mohit')
print(mydict)

# clear() 
mydict.clear()
print(mydict)