







words = ["tea", "ate", "eat"]
d = {}
for word in words:
    key = ''.join(sorted(word)) # add (word) here
    if key not in d:
        d[key] = []
    d[key].append(word)
print(list(d.values()))





n = int(input())
ids = list(map(int,input()))
freq = {}
for i in ids:
    freq[i] = freq.get(i,0)+1
result = []
for k,v in freq.items():
    if v == 1:
        result.append(k)
result.sort()
print(*result)        

