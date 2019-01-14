def get_longest_increasing_subsequence(a):
    L = [0] * len(a)
    for i, a_i in enumerate(a):
        L[i] = 1
        for j in range(0, i):
            if a[j] < a_i and L[i] < 1 + L[j]:
                L[i] = 1 + L[j]
    maximum = 1
    for i in range(1,len(a)):
        if L[i] > L[maximum]:
            maximum = i
    return L[maximum]


def main():
    a = [3,2,3,1,4,2,5,1,6,3,1]
    lis = get_longest_increasing_subsequence(a)
    print("Longest increasing subsequence: " + str(lis))


if __name__ == "__main__":
    main()