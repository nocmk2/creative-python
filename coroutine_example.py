from inspect import getgeneratorstate

def co_example(a):
    print("-> Started: a = ", a)
    b = yield a
    print("-> Received: b = ", b)
    c = yield a + b
    print("-> Received: c = ", c)


if __name__ == "__main__":
    c = co_example(14)
    print(getgeneratorstate(c))
    print(next(c))
    print(getgeneratorstate(c))
    print(c.send(28))
    print(getgeneratorstate(c))
    print(c.send(99))
    print(getgeneratorstate(c))

