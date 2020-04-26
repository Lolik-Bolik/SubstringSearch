import algorithms_substring_problem as algo


def main():
    with open('/benchamarks/good_t_1.txt', 'r') as text:
        text = text.read()
    with open('/benchamarks/good_w_1.txt', 'r') as pattern:
        pattern = pattern.read()
    # text = 'fdv'
    # pattern = 'd'
    b_m = algo.BoyerMoore(text, pattern)
    b_m.search()
    print(b_m.operation_amount)


if __name__ == '__main__':
    main()