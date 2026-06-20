arr = [90,80,90,70,,80,90]
d={}
for marks in arr:
    if marks in d:
        d[marks] += 1
    else:
        d[marks] = 1
print(d) 






n = int(input())
marks = list(map(int, input().split()))
freq = {}
for marks in marks:
    freq[marks] = freq.get(marks,0) = 1
for k, v in freq.items():
    print(k, "->", v)
    


n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c