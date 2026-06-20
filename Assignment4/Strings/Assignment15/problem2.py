n = int(input())

d = {}

for _ in range(n):
    word = input().strip()

    key = "".join(sorted(word))

    if key not in d:
        d[key] = []

    d[key].append(word)

for group in d.values():
    print("[" + " ".join(group) + "]")





 