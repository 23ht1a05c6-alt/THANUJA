A = {1, 2, 3, 4} 
B = {3, 4, 5, 6}
print(A | B)
#union


#intersaction
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A & B)




#difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A - B)




#symmetric difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A ^ B)






#bulid in method
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))





#A set A is called a subset of set B if all elements of A are present in B.
A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))





#Superset in Python Sets

#A set A is called a superset of set B if A contains all elements of B.
A = {1, 2}
B = {1, 2, 3, 4}
print(B.issubset(A))






#Frozenset

#A frozenset is an immutable version of a set.

#set → mutable (can add/remove elements)
#frozenset → immutable (cannot change elem



fs = frozenset([1, 2, 3, 4])

print(fs)

'''


orders
list is order are not order
tuple is a  order
set is Unicode
dictory is ordr



list is mutable
tuple is immutable
dictory is immutable and mutable
set is mutable
keys are immutable



'''



 

