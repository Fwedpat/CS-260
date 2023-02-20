import timeit
import sys
import pandas as pd
import matplotlib.pyplot as plt

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(sys.argv[1])

results = []
for x in range(1,n+1):
    time = timeit.timeit(lambda: fib(x), number=1000)
    results.append([x, time, fib(x)])

print(f'Time taken to calculate fib({n}) is {time} seconds')
print(f'fib({n}) = {fib(n)}')

df = pd.DataFrame(results, columns=["n", "time (s)", "result"])
print(df)


df.plot(x='n', y='time (s)', kind='line')
plt.savefig('2.png')
plt.show()
