# 所有练习的参考答案
from functools import reduce


def remove_cword(a):
    """
    练习1.1 过滤掉a中以字符'C'开头的元素
    a = ['B','NULL','ABA','CC','NULL','CA']
    """
    return filter(lambda x: not x.startswith("C"), a)


def odd_even_bit(b):
    """
    练习1.2 输出代表b中奇偶数的列表，0代表偶数，1代表奇数 预期结果：[0,1,1,0,0,1]
    b = [34, 35, 27, 16, 12, 29]
    output: [0,1,1,0,0,1]
    """
    return map(lambda x: 0 if x % 2 == 0 else 1, b)


def fib(n):
    """
    练习1.3 实现函数fib(n)当输入正整数n输出第n位斐波那契数列结果
    """
    return reduce(lambda x, _: [x[1], x[0] + x[1]], range(n - 2), [1, 1])[1]



if __name__ == "__main__":
    a = ["B", "NULL", "ABA", "CC", "NULL", "CA"]
    b = [34, 35, 27, 16, 12, 29]
    print(fib(3))
    print(list(remove_cword(a)))
    print(list(odd_even_bit(b)))
