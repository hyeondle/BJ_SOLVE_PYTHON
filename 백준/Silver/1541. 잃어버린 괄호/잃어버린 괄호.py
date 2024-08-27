import re

def min_expression_value(expression):

    nums = list(map(int, re.findall(r'\d+', expression)))
    ops = re.findall(r'[+-]', expression)
    
    n = len(nums)
    

    dp = [[float('inf')] * n for _ in range(n)]
    

    for i in range(n):
        dp[i][i] = nums[i]
    

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            for k in range(i, j):
                if ops[k] == '+':
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
                elif ops[k] == '-':
                    dp[i][j] = min(dp[i][j], dp[i][k] - dp[k + 1][j])
    
    return dp[0][n-1]

expression = input().strip()
print(min_expression_value(expression))