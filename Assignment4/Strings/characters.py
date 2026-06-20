   








n = 5
ch = 65

for i in range(1, n+1):

    temp = []

    for j in range(i):
        temp.append(chr(ch))
        ch += 1

    if i % 2 == 0:
        temp.reverse()

    for x in temp:
        print(x, end=" ")

    print()

      



    