
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





  #find longest continues sub aray   with out repecting

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





        def length_of_longest_substring(s: str) -> int:
    char_map = {}  # Stores the last known index of each character
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # If character is a duplicate and is inside the current window
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
            
        char_map[s[right]] = right
        max_len = max(max_len, right - left + 1)
         return max_len

# Example usage
print(length_of_longest_substring("abcabcbb"))  # Output: 3 (Substrings: "abc")











''''''

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





