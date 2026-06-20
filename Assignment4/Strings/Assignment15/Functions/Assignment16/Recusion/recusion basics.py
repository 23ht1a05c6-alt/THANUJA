#recusi#on is programming technique


def function(n):
    if n == 0:      # Base case
        return
    function(n-1)  # Recursive call
    

#recusive case; function call as
#base case: base condition where stop


def factorial(n):
    if n == 0:      # Base Case
        return 1
    return n * factorial(n - 1)   # Recursive Case
