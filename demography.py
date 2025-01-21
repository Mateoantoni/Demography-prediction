#!/usr/bin/env python3

import math
import sys
import csv
import string

def parser() -> list[dict]:
    with open('105demography_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")
        buffer = list(reader)
    return buffer

def main():
    buffer = parser()
    for row in buffer:
        if row["Country Code"] == sys.argv[1]:
            print(row)
            print("Country:", row["Country Name"])
            x = [int(i) for i in list(row.values())[2:]]
            y = [int(i) for i in list(row.keys())[2:]]
            print(x)
            print(y)

    n = 57
    x_list = x[2:]
    y_list = y[2:]
    

    sum_X = sum(x_list)
    sum_Y = sum(y_list)
    sum_XX = sum(x**2 for x in x_list)
    sum_YY = sum(y**2 for y in y_list)
    sum_XY = sum(x * y for x, y in zip(x_list, y_list))

    # For Fit 1 (Y = aX * X + bX)
    aX = (n * sum_XY - sum_X * sum_Y) / (n * sum_XX - sum_X**2)
    bX = (sum_Y - aX * sum_X) / n

    # For Fit 2 (X = aY * Y + bY)
    aY = (n * sum_XY - sum_Y * sum_X) / (n * sum_YY - sum_Y**2)
    aY = aY / 1000000
    bY = (sum_X - aY * sum_Y) / n
    bY = bY / 1000000

    Y_pred = []* n
    for x in x_list:
        Y_pred.append(x*aX + bX)

    RMSD = math.sqrt(sum((sum_Y - y)** 2 for y in Y_pred)) / n

    print("Fit 1")
    if bX < 0:
        bX = bX * -1
        print("Y =", "{:.2f}".format(aX), "X -", "{:.2f}".format(bX))
    else:
        print("Y =", "{:.2f}".format(aX), "X +", "{:.2f}".format(bX))
    print("Root-mean-square deviation:", "{:.2f}".format(RMSD))
    print("Population in 2050:", "nb en m")

    print("Fit 2")
    if bY < 0:
        bY = bY * -1
        print("X =", "{:.2f}".format(aY), "Y", "-", "{:.2f}".format(bY))
    else:
        print("X =", "{:.2f}".format(aY), "Y", "+", "{:.2f}".format(bY))
    print("Root-mean-square deviation:", "{:.2f}".format(RMSD))
    print("Population in 2050:", "nb en m")
if __name__ == "__main__":
    main()
