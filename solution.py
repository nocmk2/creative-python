# 所有练习的参考答案
from functools import reduce
def remove_null(): 
    a = ['B','NULL','ABA','CC','NULL','CA']
    i = filter(lambda x:x!='NULL', a)
    res = list(i)
    print(res) # ['B', 'ABA', 'CC', 'CA']

def fib(n):
    """
    练习1.3 实现函数fib(n)当输入正整数n输出第n位斐波那契数列结果
    """
    return reduce(lambda x, _: [x[1], x[0] + x[1]], range(n - 2), [1, 1])[1]

if __name__ == "__main__":
    print(fib(3))
    remove_null()
