# dynamic programming is a method of optimizing the repitative tasks while using recusrion.
# Example: Fibonacci series

# Fibonacci series (Using Recursion)

# Memoization - is Bottom to Top approach
# Tabulization - is Top to Bottom approach

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

result = fib(8)
print(result)

# Fibonacci series (Using Recursion)
# Memoization - is Bottom to Top approach
def fib(n,dp):
    # dp = 
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif dp[n] != -1 :
        return dp[n]
    else:
        dp[n] = fib(n-1,dp) + fib(n-2,dp)
        print(dp)
        return dp[n]
        
dp = [-1] * 8
result = fib(7,dp)

print(result)

# Tabulization - is Top to Bottom approach
dp = [0] * 101
for i in range(2,100):
    dp[i] = dp[i-1] + dp[i - 2]

print(dp[7],"//")
