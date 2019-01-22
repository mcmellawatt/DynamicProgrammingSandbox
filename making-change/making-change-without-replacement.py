import numpy as np

def making_change_without_replacement(v, X):
    T = np.full([len(X),v], False, dtype=bool)

    for i in range(len(X)):
        for j in range(1,v+1):
            if T[i-1,j-1] or \
                (j-X[i] >= 0 and T[i-1,j-1-X[i]]) \
                or X[i] == j:
                T[i][j-1] = True

    return T[len(X)-1][v-1]

def main():
    X = [1, 5, 10, 20]

    for i in range(1, 51):
        print("Make change for " + str(i) + "?: " + str(making_change_without_replacement(i, X)) + "\n")

if __name__ == "__main__":
    main()