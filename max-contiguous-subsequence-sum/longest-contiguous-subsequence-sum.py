import sys

def get_max_contiguous_subsequence_sum(a):
    s = [0] * len(a)

    for i in range(0, len(a)):
        s[i] = a[i]
        if s[i-1] > 0:
            s[i] = s[i] + s[i-1]

    max_global = -sys.maxsize
    for v in s:
        if v > max_global:
            max_global = v

    return max_global


def main():
    a = [5, 15, -30, 10, -5, 40, 10]
    mcss = get_max_contiguous_subsequence_sum(a)
    print("Max contiguous subsequence sum: " + str(mcss))


if __name__ == "__main__":
    main()