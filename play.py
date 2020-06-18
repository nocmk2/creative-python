import pandas as pd
import random
import numpy as np
from functools import reduce


# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html?highlight=apply#pandas.DataFrame.apply
if __name__ == "__main__":
    # l = [random.randint(0, 100) for i in range(100)]
    # def plus100(v):
    #     return v + 0.01 * random.randint(0, 100)

    # df = pd.DataFrame(np.random.random_integers(1, 100, (12, 2)), columns=["a", "b"])
    # x = df.apply()

    # dosomething = lambda x: x / 100 if x > 500 else x * 100
    # dosomething = lambda x: print(x)

    # b = lambda x: x / 100

    # # df = pd.DataFrame(np.random.randint(0, 1000, (12, 2)), columns=["a", "b"])
    # # df = df.applymap(dosomething)
    # # # df = df.apply(b)

    # # print(df)

    # def sum(a, b):
    #     return a + b

    # add = sum
    # print(add(3, 4))  # 7

    # def plus(funcb, a, b):
    #     def plus_one():
    #         return 1 + funcb(a, b)

    #     return plus_one

    # p = plus(add, 3, 4)
    # print(p)  # <function plus.<locals>.plus_one at 0x105d38170>
    # print(p())  # 8
    # plus.plus_one(3, 4)  # AttributeError: 'function' object has no attribute 'plus_one'

    # def handle_t(v):
    #     return str(v + 1) + "C"

    # temp = map(handle_t, a)
    # print(list(temp))  # ['35C', '36C', '28C', '17C', '13C', '30C']
    # a = [1, 2, 3]

    # up = 0

    # def a():
    #     up += 1

    # a()
    # print(up)

    a = [1800, 1900, 800, 1800, 900, 1900]
    up, down = 0, 0

    def f(a1, a2):
        global up, down
        c = a2 - a1
        if c >= 0:
            up += c
        else:
            down += c
        return a2

    reduce(f, a)
    print(up)
    print(down)
# print(a + 3)
# pandas
# pandas.DataFrame.apply
# pandas.DataFrame.applymap

# python
# map
# apply
# filter

a = ["B", "NULL", "ABA", "CC", "NULL", ""]

print(list(filter(lambda x: not x.startswith("C"), a)))
