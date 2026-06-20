   
    




T = int(input())

for _ in range(T):
    S = input().strip()
    K = int(input().strip())
    
    n = len(S)
    result = []

    for i in range(K):
        result.append(S[i % n])

    print("".join(result))






 #remove all adjacent duplicates



S = "abbaca" 

  



