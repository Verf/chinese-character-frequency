# -*- coding: utf-8 -*-
from pathlib import Path
from multiprocessing import freeze_support
from concurrent.futures import ProcessPoolExecutor


def char_count(path):
    char_count = {}
    with open(path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            for c in line:
                if "\u4e00" <= c <= "\u9fff":
                    if c not in char_count:
                        char_count[c] = 0
                    char_count[c] += 1
    return char_count


def main():
    files = Path("./data").iterdir()
    char_dict = {}
    with ProcessPoolExecutor() as pool:
        for d in pool.map(char_count, files):
            for k, v in d.items():
                if k in char_dict:
                    char_dict[k] += v
                else:
                    char_dict[k] = v
    ordered_char_dict = dict(
        sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    )
    with open(
        "./chinese_character_frequency.txt", "w", encoding="utf-8", newline="\n"
    ) as fw:
        for c, o in ordered_char_dict.items():
            fw.write(f"{c}\t{o}\n")


if __name__ == "__main__":
    freeze_support()
    main()
