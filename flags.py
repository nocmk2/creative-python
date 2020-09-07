import os
import time
import sys

import requests

from concurrent import futures

POP20_CC = (
    "CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR".split()
)

BASE_URL = "http://localhost:8021/"

DEST_DIR = "downloads/"
MAX_WORKERS = 20


def save_flag(img, filename):
    path = os.path.join(DEST_DIR, filename)
    with open(path, "wb") as fp:
        fp.write(img)


def get_flag(cc):
    url = "{}/{cc}/{cc}.gif".format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=" ")
    sys.stdout.flush()


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + ".gif")
    return cc


def download_many_seq(cc_list):
    for cc in sorted(cc_list):
        download_one(cc)

    return len(cc_list)


def download_many_futures(cc_list):
    workers = max(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, cc_list)

    return len(list(res))

def download_many_submit(cc_list):
    cc_list = cc_list[:5]
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)
    
    return len(results)


def main():
    t0 = time.time()
    count = download_many_seq(POP20_CC)
    elapsed = time.time() - t0
    msg = "\n{} flags downloaded by sequence in {:.6f}s"
    print(msg.format(count, elapsed))

    t1 = time.time()
    count = download_many_futures(POP20_CC)
    elapsed = time.time() - t1
    msg = "\n{} flags downloaded by ThreadPoolExecutor in {:.6f}s"
    print(msg.format(count, elapsed))

    t2 = time.time()
    count = download_many_submit(POP20_CC)
    elapsed = time.time() - t2
    msg = "\n{} flags downloaded by ThreadPoolExecutor submit in {:.6f}s"
    print(msg.format(count, elapsed))
    # Deferred class in Twisted
    # Future 类类似Twisted类中的Deferred类 Tornado中的Future类 JS中的Promise对象


if __name__ == "__main__":
    main()
