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
    if len(sys.argv) < 2:
        print("Usage: python script.py <Country Code>")
        return 84
    
    buffer = parser()
    for row in buffer:
        if row["Country Code"] == sys.argv[1]:
            print("Country:", row["Country Name"])
            x = [int(i) for i in list(row.values())[2:]]
            y = [int(i) for i in list(row.keys())[2:]]
    x_list = y
    y_list = x
    n = len(x_list)
    
    sum_X = sum(x_list)
    sum_Y = sum(y_list)
    sum_XX = sum(x**2 for x in x_list)
    sum_YY = sum(y**2 for y in y_list)
    sum_XY = sum(x * y for x, y in zip(x_list, y_list))

    # For Fit 1 (Y = aX * X + bX)
    aX = (n * sum_XY - sum_X * sum_Y) / (n * sum_XX - sum_X * sum_X)
    bX = (sum_Y * sum_XX - sum_X * sum_XY) / (n * sum_XX - sum_X * sum_X)
    aX = aX / 1000000
    bX = bX / 1000000


    # For Fit 2 (X = aY * Y + bY)
    aY = (n * sum_XY - sum_X * sum_Y) / (n * sum_YY - sum_Y * sum_Y)
    bY = (sum_X * sum_YY - sum_Y * sum_XY) / (n * sum_YY - sum_Y * sum_Y)
    aY = aY * 1000000

    Y_pred = [aX * x + bX for x in x_list]
    RMSD_x = math.sqrt(sum((y - y_pred)**2 for y, y_pred in zip(y_list, Y_pred)) / n)

    X_pred = [aY * y + bY for y in y_list]
    RMSD_y = math.sqrt(sum((x - x_pred)**2 for x, x_pred in zip(x_list, X_pred)) / n)

    print("Fit 1")
    if bX < 0:
        bX = bX * -1
        print("Y =", "{:.2f}".format(aX), "X -", "{:.2f}".format(bX))
    else:
        print("Y =", "{:.2f}".format(aX), "X +", "{:.2f}".format(bX))
    print("Root-mean-square deviation:", "{:.2f}".format(RMSD_x))
    print("Population in 2050:", "nb en m")

    print("Fit 2")
    if bY < 0:
        bY = bY * -1
        print("X =", "{:.2f}".format(aY), "Y", "-", "{:.2f}".format(bY))
    else:
        print("X =", "{:.2f}".format(aY), "Y", "+", "{:.2f}".format(bY))
    print("Root-mean-square deviation:", "{:.2f}".format(RMSD_y))
    print("Population in 2050:", "nb en m")
if __name__ == "__main__":
    main()
