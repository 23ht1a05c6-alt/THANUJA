import sys

def solve():
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        
        total_sum = sum(arr)
        
        full_cycles = k // n
        rem = k % n
        
        result = full_cycles * total_sum
        
        for i in range(rem):
            result += arr[i]
        
        print(result)

solve()