import time

a = ['B','NULL','ABA','CC','NULL','CA']


if __name__ == "__main__":
    RUNNING_TIMES=1000000
    start = time.time()
    for i in range(RUNNING_TIMES):
        res = filter(lambda x:x!='NULL',a)
        res = list(res)

    t1 = time.time()-start

    start = time.time()
    for i in range(RUNNING_TIMES):
        res = []
        for x in a:
            if x!='NULL':
                res.append(x)
    t2 = time.time()-start

    start = time.time()
    for i in range(RUNNING_TIMES):
        res = [x for x in a if x!='NULL']
    t3 = time.time()-start

    print("t1: {:.4f} seconds".format(t1))
    print("t2: {:.4f} seconds".format(t2))
    print("t3: {:.4f} seconds".format(t3))

