def factorial(hello):
    if hello == 0:      # Base Case
        return 1
    return n * factorial(hello - 1)   # Recursive Case




def hello(n):
    if n==0:  #base condition
        return
    print("hello")
    #recursive call
    hello(n-1)
hello(5)





#call stack
def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n-1)

count_down(3)





def sum_n(n):
    if n == 1:      # Base Case
        return 1
    return n + sum_n(n - 1)   # Recursive Case

print(sum_n(5))




#Fibonacci Series Using Recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i), end=" ")



def reverse_string(s):
    if len(s) <= 1:      # Base Case
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))





def is_palindrome(s):
    if len(s) <= 1:      # Base Case
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])   # Recursive Case

s = "madam"

if is_palindrome(s):
    print("Palindrome")
else:
    print("Not Palindrome")




def is_palindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])





