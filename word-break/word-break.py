# Recurrence for this DP problem is:
# w[i] = true if w[j] = true & dict[j:i] for some j between 0 and i - 1
def word_break(s, dict):
    w = [False] * (len(s) + 1)
    w[0] = True

    for i in range(0,len(s)+1):
        for j in range(0,i):
            if w[j] and s[j:i] in dict:
                w[i] = True

    return w[len(s)]

def main():
    word_dict = ["it", "was", "the", "best", "of", "times"]
    s = "itwasthebestoftimes"
    print("Can be reconstructed? " + str(word_break(s, word_dict)))


if __name__ == "__main__":
    main()