import re

if __name__ == "__main__":
    rich = [
        "Tom$$$",
        "Jack$$$$$$$",
        "Aris$$$$$$$",
        "Jay$$",
        "Tom$$$$$$$$$",
        "Jerry$$$",
    ]
    the_richest = sorted(
        rich, key=lambda x: len(re.sub(r"[^$]", "", x)), reverse=True
    )
    print(
        the_richest
    )  # ['Tom$$$$$$$$$', 'Jack$$$$$$$', 'Aris$$$$$$$', 'Tom$$$', 'Jerry$$$', 'Jay$$']

