import algorithms as algo


def main():
    with open('/benchmarks/bad_t_3.txt', 'r') as text:
        text = text.read()
    with open('/benchmarks/bad_w_3.txt', 'r') as pattern:
        pattern = pattern.read()
    #text = 'fdv'
    #pattern = 'd'
    b_m = algo.BoyerMoore(text, pattern)
    b_m.search()
    print(b_m.operation_amount)


if __name__ == '__main__':
    main()