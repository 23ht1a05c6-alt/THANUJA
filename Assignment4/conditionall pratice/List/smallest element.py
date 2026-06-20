nums = [10,20,30,40]
print(min(nums))#prit a list


#find length of a list
nums = [10,20,30,40]
print(len(nums))



#sum of elements
nums = [10,20,30,40]
print(sum)




#largest element
nums = [10,20,30,40]
print(max(nums))





#smallest element
nums = [10,20,30,40]
print(min(nums))





#reverse a list
nums = [10,20,30,40]
print(nums[::-1])




#search an element
nums = [10,20,30,40]
if 20 in nums:
    print("found")
else:
    print("not found") 






#remve an lement
nums = [10,20,30,40]
nums . remove(40)
print(nums)






#sort a list
nums = [10,20,30,40]
nums.sort()
print(nums)







#merge two lst
num1 = [1,2,3]
num2 = [4,6,7]
num3=num1+num2
print(num3)




#count even and odd numbers
even = 0
odd = 0
for i in nums:
    if i % 2 == 0:
        even += 1
    
    else:
        odd += 1 
print("even=" , + even) 
print("odd =" , + odd)  






##add an element
nums = [10,20,30,40]
nums.append(40)
print(nums)




#factorial of a large number
n = 100
fact = 1
for i in range(1, n+1)
    fact += 1
print(fact)






#search an element
nums = [10,20,3040]
if 20 in nums:
    print("found")
else:
    print("not found")





#check whether a lisr is palindrome or not
nums = [1,2,3,2,1]
if nums == nums[::-1]:
    print("palindrome")
else:
    print("not a palindrome")





#find  pairs whose sum equal a give number
nums = [1,2,3,4,5,6]
target = 7
for i in range(len(nums)):
    for j in range( i + 1len(nums)):
        if nums









# untill thenr is increaasd
[12:57 pm, 2/6/2026] Ratna 🐶: Vachava
[10:35 am, 3/6/2026] Ratna 🐶: 
arr =[1,4,20,3,10]
target = 33
left = 0
current_sum = 0
for right in range(len(arr)):
        current_sum = current_sum+arr[right]
        while current_sum > target:
            current_sum = current_sum - arr[left]
            left = left + 1
        if current_sum == target:
            print("Sum found between indexes", left, "and", right)
            break





        arr =[1,4,20,3,10]
target = 33
left = 0
current_sum = 0
for right in range(len(arr)):
        current_sum = current_sum+arr[right]
        while current_sum > target:
            current_sum = current_sum - arr[left]
            left = left + 1
        if current_sum == target:
            print(arr[left:right+1])
            break






n = 100
fact = 1
for i in range(1, n+1)
   fact *= 1
print(fact)





def median_diff(a,b):
    merged = sorted(a+b)

    n = len(merged)

    if n%2:
        return merged[n//2]

    return (merged[n//2-1]+merged[n//2])/2

print(median_diff([1,3],[2]))