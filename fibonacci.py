
def fibonacci(n, dict_memo = {}):
    if n in dict_memo : return dict_memo[n]
    if n <= 2: return 1;
    dict_memo[n] = fibonacci(n-1, dict_memo) + fibonacci(n-2, dict_memo)
    return dict_memo[n]
print(fibonacci(150))

