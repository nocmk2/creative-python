# 所有练习的参考答案
from functools import reduce


def fib(n):
    """
    练习1.3 实现函数fib(n)当输入正整数n输出第n位斐波那契数列结果
    """
    return reduce(lambda x, _: [x[1], x[0] + x[1]], range(n - 2), [1, 1])[1]


print(fib(3))
