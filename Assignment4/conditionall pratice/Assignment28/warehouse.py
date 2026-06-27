'''
s = int(input())
products = set()
for _ in range(s):
    x = int(input())
    if x > 0:
        products.add(x)
    else:
        products.discard(-x)  
print(len(products))          


s = int(input())
balance = 0
suspicious = False
for i in range(s):
    transaction = int(input())
    balance += transaction
    if balance< 0:
        suspicious = True
if suspicious:
    print("YES")        
else:
    print("NO")
               


n = int(input())
arr = list(map(int, input().split()))
limit = int(input())
left = 0
current_sum = 0
max_count = 0
for right in range(n):
    current_sum += arr[right]
    while current_sum > limit:
        current_sum -= arr[right]
        left += 1
    max_count = max(max_count, right-left+1) 
print(max_count) 





logins = input().strip()
count = 0
alert = False
for ch in logins:
    if ch == 'F':
        count += 1
        if count >= 3:
            alert = True
            break
        else:
            cout = 0
if alert:
    print("ALERT") 
else:
    print("SAFE")

'''


