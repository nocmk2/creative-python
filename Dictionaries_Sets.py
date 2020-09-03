from collections import abc
from collections import UserDict
import pandas as pd
from types import MappingProxyType
from timeit import default_timer as timer

if __name__ == "__main__":
    # Collection<--Mapping<--MutableMapping
    # a = (1, 2, 3)
    # print(hash(a))
    # b = [1, 2, 3]
    # b.append(4)
    # print(b)
    # d = {a: 1, "b": 2}
    # print(isinstance(a, abc.Mapping))
    # print(isinstance(a, abc.MutableMapping))
    # tf = (1, 2, frozenset([30, 40]))
    # # hash(tf)
    # a = frozenset([30,40])
    # print(a)
    # a = dict(one=1, two=2, three=3)
    # b = {"three": 3, "two": 2, "one": 1}
    # b.popitem()
    # print(b)
    tmp = {
        "a": [
            {"a1": "tom"},
            {"a2": "jery"},
            {"a3": "jery"},
            {"a4": "cao"},
            {"a5": "cao"},
        ],
        "b": [{"b1": "lily"}, {"b2": "lily"}, {"bn": "jack"},],
    }

    class V:
        def __init__(self, d):
            self.__data = d

        @classmethod
        def __first_value(cls, dic_data):
            return next(iter(dic_data.items()))[1]

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return V.__first_value(self.__data) == V.__first_value(other.__data)
            else:
                return False

        def __hash__(self):
            return 1

        def to_dict(self):
            return self.__data

    # https://www.v2ex.com/t/701703#reply13
    # https://learning.oreilly.com/library/view/Fluent+Python,+2nd+Edition/9781492056348/ch03.html#set_ops_dict_views_sec
    def dict_value_remove_duplicate(data):
        res = {}
        for key in data:
            s = set()
            for record in data[key]:
                s.add(V(record))
            res[key] = [e.to_dict() for e in s]
        return res

    def drop_duplicates(l):
        return [x.to_dict() for x in set([V(record) for record in l])]

    def v5(data):
        return {key: drop_duplicates(value) for (key, value) in data.items()}

    def v2(data):
        ret = {}
        for key, items in data.items():
            exists_values = set()
            ret[key] = []
            for item in items:
                item_val = next(iter(item.items()))[1]
                if item_val not in exists_values:
                    exists_values.add(item_val)
                    ret[key].append(item)
        return ret

    def v3(tmp):
        return dict(
            [
                (
                    k,
                    dict(
                        [
                            (n, m)
                            for m, n in dict(
                                [reversed(next(iter(i.items()))) for i in v]
                            ).items()
                        ]
                    ),
                )
                for k, v in tmp.items()
            ]
        )

    def v4(tmp):
        return {
            key: list(
                reversed(
                    [
                        {v: k}
                        for k, v in {
                            y: x for d in reversed(val) for x, y in d.items()
                        }.items()
                    ]
                )
            )
            for key, val in tmp.items()
        }

    start = timer()
    res = dict_value_remove_duplicate(tmp)
    end = timer()
    print(end - start)
    # print(tmp)

    start = timer()
    res2 = v2(tmp)
    end = timer()
    print(end - start)

    start = timer()
    res3 = v3(tmp)
    end = timer()
    print(end - start)

    start = timer()
    res4 = v4(tmp)
    end = timer()
    print(end - start)

    start = timer()
    res5 = v5(tmp)
    end = timer()
    print(end - start)

    print(res)
    print(res2)
    print(res3)
    print(res4)
    print(res5)

    a = (1, 2, 3)
    print(tuple(reversed(a)))

    print("*" * 80)

    l = [{"a": 1}, {"b": 2}, {"c": 3}]

