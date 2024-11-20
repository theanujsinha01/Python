# tuples in Python are immutable, meaning you cannot change their content after creation. Once a tuple is created, its elements cannot be modified, added, or removed.



#Tuple : similar to list but can't modified once created

a = (1,5,8)
print(a)

# count() : count the frequency of specific item
tuple_1 = (1,2,4,2,2,9)
print(tuple_1.count(2))

#index() : search a specific value and give index
ans = tuple_1.index(9)
print(ans)

# length of tuple
print(len(tuple_1))



