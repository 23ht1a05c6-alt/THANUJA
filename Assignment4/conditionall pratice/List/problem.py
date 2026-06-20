

#problem3:find the length of longest cotinues sub array that contains no repeating elements
#input:[1,2,3,1,2,3,4]
#output:4
arr = [1,2,3,1,2,3,4]
left = 0
max_length = 0
for right in range(len(arr)):
    while arr[right] in arr[left:right]:
        left = left + 1
    max_length = max(max_length,right-left+1)
print(max_length)






#find the longest non repecting substring]
def find_longest_substring(s: str) -> str:
    char_map = {}
    left = 0
    start_idx = 0
    max_len = 0
    
    for right, char in enumerate(s):
        # Jump left pointer if duplicate is inside current window
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
            
        char_map[char] = right
        
        # Track the longest window boundaries
        if (right - left + 1) > max_len:
            max_len = right - left + 1
            start_idx = left
            
    return s[start_idx:start_idx + max_len]

# Test
print(find_longest_substring("pwwkew"))  # Output: "wke"
def find_longest_substring(s: str) -> str:
    char_map = {}
    left = 0
    start_idx = 0
    max_len = 0
    
    for right, char in enumerate(s):
        # Jump left pointer if duplicate is inside current window
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
            
        char_map[char] = right
        
        # Track the longest window boundaries
        if (right - left + 1) > max_len:
            max_len = right - left + 1
            start_idx = left
            
    return s[start_idx:start_idx + max_len]

# Test
print(find_longest_substring("pwwkew"))  # Output: "wke"





#Implementation of List

#A list is a collection of items stored in a specific order.
fruits = ["apple", "banana", "orange"]
print(fruits)



#2. Sequence Type
s = "Python"

print(s[0])      # Indexing
print(s[1:4])    # Slicing
print(len(s))    # Length




#3. Mutable and Immutable Objects
a = [1, 2, 3]
a.append(4)

print(a)






#ex:
#input:"abcabcbb"
#output:3
s = "abcabcbb"
left = 0

max_length = 0
seen = set()

for right in range(len(s)):
    while s[right] in seen:
        seen.remove(s[left])
        left =left + 1
    seen.add(s[right])
    max_length = max(max_length, right - left + 1)

print(max_length)






#silcing windows
nums = [1,2,5,7,6]
print(nums[-1:3:2])



#sorted order
nums = [10,0,-1,7,8,10,-67]
nums.sort()
print(nums)




nums = [10,0,-1,7,8,10,-67]
#nums.reverse()
print(max(nums))





nums = [10,0,-1,7,8,10,-67]
nums[1:4]=[45,46,47]
print(nums)




#extend
nums = [10,0,-1,7,8,10,-67]
nums.extend([45,46,47])
print(nums)





nums = [1, 2, 3, 2, 4, 1, 5]

freq = {}

for num in nums:
    freq[num] = freq.get(num, 0) + 1

for key, value in freq.items():
    if value > 1:
        print(key)
