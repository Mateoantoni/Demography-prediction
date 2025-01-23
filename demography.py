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

def calculate_RMSD_X(x_list, y_list, n):
    # Sum of everything nedded for a and b
    sum_X = sum(x_list)
    sum_Y = sum(y_list)
    sum_XX = sum(x**2 for x in x_list)
    sum_YY = sum(y**2 for y in y_list)
    sum_XY = sum(x * y for x, y in zip(x_list, y_list))
    # For Fit 1 (Y = aX * X + bX)
    aX = (n * sum_XY - sum_X * sum_Y) / (n * sum_XX - sum_X * sum_X)
    bX = (sum_Y * sum_XX - sum_X * sum_XY) / (n * sum_XX - sum_X * sum_X)
    # Final operation to get RMSD
    RMSD_x = math.sqrt(sum([(y_list[i]-aX*x_list[i]-bX)**2 for i in range(n)]) / n)
    return RMSD_x, aX, bX

def calculate_RMSD_Y(x_list, y_list, n):
    # Sum of everything nedded for a and b
    sum_X = sum(x_list)
    sum_Y = sum(y_list)
    sum_XX = sum(x**2 for x in x_list)
    sum_YY = sum(y**2 for y in y_list)
    sum_XY = sum(x * y for x, y in zip(x_list, y_list))
    # For Fit 2 (X = aY * Y + bY)
    aY = (n * sum_XY - sum_X * sum_Y) / (n * sum_YY - sum_Y * sum_Y)
    bY = (sum_X * sum_YY - sum_Y * sum_XY) / (n * sum_YY - sum_Y * sum_Y)
    # Final operation to get RMSD
    RMSD_y = math.sqrt(sum([(y_list[i]-(x_list[i]-bY)/aY)**2 for i in range(n)]) / n)
    return RMSD_y, aY, bY

def calculate_correlation(X, Y):
    # Step 1: Calculate the means
    mean_X = sum(X) / len(X)
    mean_Y = sum(Y) / len(Y)

    # Step 2: Calculate deviations and products
    numerator = sum((x - mean_X) * (y - mean_Y) for x, y in zip(X, Y))
    sum_square_X = sum((x - mean_X) ** 2 for x in X)
    sum_square_Y = sum((y - mean_Y) ** 2 for y in Y)

    # Step 3: Calculate r
    denominator = (sum_square_X * sum_square_Y) ** 0.5
    r = numerator / denominator if denominator != 0 else 0

    return r

def main():
    argc = len(sys.argv)
    if argc < 2:
        return 84
    if sys.argv[1] == "-h":
        print("Usage: python script.py <Country Code>")
        return 84
    
    buffer = parser()
    for row in buffer:
        if row["Country Code"] == sys.argv[1]:
            print("Country:", row["Country Name"])
            y_list = [int(i) * 0.000001 for i in list(row.values())[2:]]
            x_list = [int(i) for i in list(row.keys())[2:]]
    n = len(x_list)

    RMSD_x, aX, bX = calculate_RMSD_X(x_list, y_list, n)
    RMSD_y, aY, bY = calculate_RMSD_Y(x_list, y_list, n)

    x = 2050
    Y_estim = (aX * x) + bX
    X_estim = (x - bY) / aY

    Correlation = calculate_correlation(x_list, y_list)

    print("Fit 1")
    if bX < 0:
        bX = bX * - 1
        print("    Y =", "{:.2f}".format(aX), "X -", "{:.2f}".format(bX))
    else:
        print("    Y =", "{:.2f}".format(aX), "X +", "{:.2f}".format(bX))
    print("    Root-mean-square deviation:", "{:.2f}".format(RMSD_x))
    print("    Population in 2050:", "{:.2f}".format(Y_estim))

    print("Fit 2")
    if bY < 0:
        bY = bY * -1
        print("    X =", "{:.2f}".format(aY), "Y", "-", "{:.2f}".format(bY))
    else:
        print("    X =", "{:.2f}".format(aY), "Y", "+", "{:.2f}".format(bY))
    print("    Root-mean-square deviation:", "{:.2f}".format(RMSD_y))
    print("    Population in 2050:", "{:.2f}".format(X_estim))
    print("Correlation:", "{:.4f}".format(Correlation))

if __name__ == "__main__":
    main()
