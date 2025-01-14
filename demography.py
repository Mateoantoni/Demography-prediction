#!/usr/bin/env python3

import math
import sys
import csv

def parser():
    with open('105demography_data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(', '.join(row))
        return reader

def printer():
    if sys.argv[1] == "-h":
        print("USAGE\n    ./105demography [code]+\n\nDESCRIPTION\n    code    country code")
    exit

def main():
    printer()
    reader = parser()
    i = 0
    j = 0
    n = 59
    x_list = [1, 2, 3, 4, 5]
    y_list = [] * n
    while reader != "\n":
        while reader != ';':
            y_list[j]
        j+=1


    sum_X = sum(x_list)
    sum_Y = sum(y_list)
    sum_XX = sum(x**2 for x in x_list)
    sum_YY = sum(y**2 for y in y_list)
    sum_XY = sum(x * y for x, y in zip(x_list, y_list))

    a = (sum_XY - sum_X * sum_Y) / (sum_XX - (sum_X)**2)
    b = (sum_Y - (a * sum_X)) / n

    Y_pred = []*n
    for x in x_list:
        Y_pred.append(x*a + b)

    RMSD = math.sqrt(sum((sum_Y - y)** 2 for y in Y_pred)) / n

    print(f"Xval (a): {a}")
    print(f"+val (b): {b}")
    print(sum_X)
    print(sum_Y)
    print(sum_XX)
    print(sum_YY)
    print(sum_XY)
    print(RMSD)


if __name__ == "__main__":
    main()