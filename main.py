import algorithms as algo


def main():
    with open('./benchmarks/bad_t_1.txt', 'r') as text:
        text = text.read()
    with open('./benchmarks/bad_w_1.txt', 'r') as pattern:
        pattern = pattern.read()
    #text = 'fdv'
    #pattern = 'd'
    b_m = algo.BruteForce(text, pattern)
    result = b_m.search()
    print(result)


if __name__ == '__main__':
    main()