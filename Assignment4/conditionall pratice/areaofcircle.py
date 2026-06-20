def zero_sum_subarray(arr):
    s = 0
    seen = set()

    for num in arr:
        s += num

        if s == 0 or s in seen:
            return True

        seen.add(s)

    return False

print(zero_sum_subarray([4,2,-3,1,6]))













