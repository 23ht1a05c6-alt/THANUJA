def median_diff(a,b):
    merged = sorted(a+b)

    n = len(merged)

    if n%2:
        return merged[n//2]

    return (merged[n//2-1]+merged[n//2])/2

print(median_diff([1,3],[2]))