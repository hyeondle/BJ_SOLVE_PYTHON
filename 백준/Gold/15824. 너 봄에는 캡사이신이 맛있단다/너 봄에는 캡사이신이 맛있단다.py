MOD = 1000000007

def solve(arr):
    n = len(arr)
    arr.sort()
    
    pow2 = [1] * n
    for i in range(1, n):
        pow2[i] = (pow2[i-1] * 2) % MOD
    
    result = 0
    for i in range(n):
        max_contribution = (arr[i] * pow2[i]) % MOD
        min_contribution = (arr[i] * pow2[n-1-i]) % MOD
        result = (result + max_contribution - min_contribution) % MOD
    
    return result


n = int(input())
arr = list(map(int, input().split()))


print(solve(arr))