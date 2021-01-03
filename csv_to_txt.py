# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd


def read_csv_column(csv_path, column_name):
    df = pd.read_csv(csv_path, encoding='utf-8', low_memory=False)
    return df[column_name].tolist()


if __name__ == "__main__":

    for i in range(10):
        units = read_csv_column("./trump/trump_" + str(i + 1) + ".csv", "微博正文")

        with open("./trump/trump_" + str(i + 1) + ".txt", "a") as file:
            for unit in units:
                file.write(unit)
        file.close()
