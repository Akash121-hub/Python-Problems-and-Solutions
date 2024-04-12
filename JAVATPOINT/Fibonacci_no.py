# The recurrence relation defines a Fibonacci number as shown below:

# Fn = Fn - 1 + Fn - 2

def fibonacci_no_by_recursion(num):
    if num < 0:
        print("Invalid num")
    elif num == 0:
        return(0)
    elif num == 1:
        return (1)
    else:
        return (fibonacci_no_by_recursion(num - 1) + fibonacci_no_by_recursion (num - 2))

print(fibonacci_no_by_recursion(4))