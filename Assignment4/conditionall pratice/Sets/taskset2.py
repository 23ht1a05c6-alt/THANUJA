#create a set square of number try to repect the square two times and muliples of 
##reate the list



A = {1,7,5,9}
B = {1,8,4,2}
print(A|B)
A = {1,7,5,9}
B = {1,8,4,2}
print(A-B)
A = {1,7,5,9}
B = {1,8,4,2}
print(A&B)
A = {1,7,5,9}
B = {1,8,4,2}
print(A^B)




##find the length of longest sequence
#input100 200 1,2
arr = [100, 200, 1, 2]

s = set(arr)
longest = 0

for num in s:
    if num - 1 not in s:  # start of sequence
        length = 1
        while num + length in s:
            length += 1
        longest = max(longest, length)

print(longest)







