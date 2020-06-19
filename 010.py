if __name__ == "__main__":
    a = ["B", "NULL", "ABA", "CC", "NULL", "CA"]
    i = filter(lambda x: not x.startswith("C"), a)
    res = list(i)
    print(res)  # ['B', 'ABA', 'CC', 'CA']

