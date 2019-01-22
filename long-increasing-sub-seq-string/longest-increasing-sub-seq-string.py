#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

def longest_increasing_sub_seq_string(X, Y):
    T = np.zeros((len(X),len(Y)))
    for i, x_i in enumerate(X):
        for j, y_j in enumerate(Y):
            if X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = T[i][j-1]
    return np.amax(T)

def main():
    X = "ABDBABFGD"
    Y = "BETFDBFAFR"
    print(longest_increasing_sub_seq_string(X, Y))

if __name__ == "__main__":
    main()