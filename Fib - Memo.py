import timeit
import sys
import pandas as pd
import matplotlib.pyplot as plt


def fib(n, memo):
    if memo[n] != -1:
        return memo[n]
    if n == 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def fib_memo(n):
    memo = [-1] * 1000
    return fib(n, memo)

results = []


n = int(sys.argv[1])
for x in range(1,n+1):
    time = timeit.timeit(lambda: fib_memo(x), number=1000)
    results.append([x, time, fib_memo(x)])

print(f'Time taken to calculate fib({n}) is {time} seconds')
print(f'fib({n}) = {fib_memo(n)}')

df = pd.DataFrame(results, columns=["n", "time (s)", "result"])
print(df)

df.plot(x='n', y='time (s)', kind='line')
plt.savefig('2.png')
plt.show()
