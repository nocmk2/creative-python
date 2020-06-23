from functools import reduce

# 练习1.3
fib = lambda n: reduce(lambda x, _: [x[1], x[0] + x[1]], range(n - 2), [1, 1])[1]

