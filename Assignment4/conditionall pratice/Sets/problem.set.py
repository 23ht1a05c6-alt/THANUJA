nums = {1, 2, 2, 3, 4, 4, 5}
print(nums)





s = {1, 2, 3}

s.add(4)      # Modify set
s.remove(2)   # Modify set

print(s)
#fixed indexing set is mutable
#we can use build in methods






s = {1, 2, 3}
s.add(4)

print(s)




#update
s = {1, 2}
s.update([3, 4, 5])

print(s)





#remove
s = {1, 2, 3}
s.remove(2)

print(s)





# discard()
s = {1, 2, 3}
s.discard(5)
print(s)




#difference between remove and discard
#discard can use in with error comeing
#remove will be come in here likeclear
#pop can be used  delates the random elment
#clear method means;-
#




s = {10, 20, 30}

print(s.pop())
print(s)

