  






s = input()

d = {}

for ch in s:
    d[ch] = d.get(ch, 0) + 1

freq = list(d.values())

if len(set(freq)) == 1:
    print("YES")
else:
    print("NO")  







    n = int(input())
ids = list(map(int, input().split()))

freq = {}

for i in ids:
    freq[i] = freq.get(i, 0) + 1

result = []

for k, v in freq.items():
    if v == 1:
        result.append(k)

result.sort()

print(*result)






   

