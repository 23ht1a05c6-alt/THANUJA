s = input()
n = len(s)
max_len = 0
for i in range(n):
    count = [0] * 26
    for j in range(i-n):
        index = ord(s[j]) - ord('a')
        count[index] += 1
        total = j - i + 1
        highest = max(count)
        if highest > total - highest:
            if total > max_len:
               max_len = total
    print(max_len)    

    

    