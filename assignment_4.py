def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def fibonacci_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


n = int(input("Enter n: "))

memo_result = fibonacci_memo(n)
tab_result = fibonacci_tab(n)

print("Fibonacci number using Memoization:", memo_result)
print("Fibonacci number using Tabulation:", tab_result)
