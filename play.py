import pandas as pd
import numpy as np
import math

from functools import reduce

# DRY Don't repeat yourself
# Decoupling
if __name__ == "__main__":
    # df = pd.DataFrame(
    #     [[4, 9, 3], [7, 8, 1], [5, 3, -1]], columns=["A", "B", "C"]
    # )
    # print(df)

    # print("=" * 90)

    # def modelA(x):
    #     # return [1.5 * x[0] + math.pi * x[1] + x[2], x[0] + x[1] + x[2]]
    #     # return pd.Series([sum(x), 1.5 * x[0] + math.pi * x[1] + x[2], "每日数据"])
    #     return [sum(x), 1.5 * x[0] + math.pi * x[1] + x[2], "每日数据"]

    # print("=" * 90)

    # df2 = df.apply(modelA, axis=1, result_type="expand")
    # # df2.rename(columns={0: "efef", 1: "heelojfi"}, inplace=True)
    # print(df2)

    def test_fruit_in_order(series):
        if series["fruit"].lower() in series["order"].lower():
            return series
        # return pd.Series(["333", "33"])
        # return ["333", None]
        return np.nan

    data = pd.DataFrame(
        {
            "fruit": ["orange", "lemon", "mango"],
            "order": ["I like orange", "Mango please?", "May i have a mango?"],
        }
    )

    print(data)

    d = data.apply(test_fruit_in_order, axis=1)
    # d.dropna(inplace=True)
    # print(d)

    mask = [
        a.lower() in b.lower() for (a, b) in data[["fruit", "order"]].values
    ]

    print(data[mask])
