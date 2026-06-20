s = input()
n = len(s)
answer = -1
for i in range(n):
    if s == s[::-1]:
        answer = i
        break
    s = s[1:] + s[0]
print(answer)    