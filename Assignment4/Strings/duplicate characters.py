s = "tanuja"
d = {}
for ch in s
     d[ch] = d.get(ch,0) + 1
for k, v in d.items():
    if v>1:
        print(k) 







s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("anagram")
else:
    print("not anagram")    