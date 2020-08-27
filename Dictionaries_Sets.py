from collections import abc
from collections import UserDict
import pandas as pd
from types import MappingProxyType

if __name__ == "__main__":
    # Collection<--Mapping<--MutableMapping
    a = (1, 2, 3)
    print(hash(a))
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
    a = dict(one=1, two=2, three=3)
    b = {"three": 3, "two": 2, "one": 1}
    b.popitem()
    print(b)
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

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return hash(id(self.__data)) == hash(id(other.__data))
            else:
                return False

        def __hash__(self):
           return 1 

        def to_dict(self):
            return self.__data
        
    # https://www.v2ex.com/t/701703#reply13
    # https://learning.oreilly.com/library/view/Fluent+Python,+2nd+Edition/9781492056348/ch03.html#set_ops_dict_views_sec
    # tmp["a"] = 

    # print(tmp["a"])
    # s = set()
    # for k in tmp["a"]:
    #     # s.add(next(iter(k.values())))
    #     s.add(V(k))
    # x = set(tmp["a"])
    # print(x)
    # y = [V(x) for x in tmp["a"]]
    # print(list(set(y)))
    
    # a = 78787 
    # print(hash(a))

    # for x in (1,1,2,2,3,3,4,4):
    #     s.add(x)

    # print(s)

