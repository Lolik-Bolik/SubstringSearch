import algorithms as algo


def main():
    with open('/home/alexslav/HSE_STUFF/Burashnikov/SubstringSearch/benchmarks/bad_t_4.txt', 'r') as text:
        text = text.read()
    with open('/home/alexslav/HSE_STUFF/Burashnikov/SubstringSearch/benchmarks/bad_w_4.txt', 'r') as pattern:
        pattern = pattern.read()
    #text = 'fdv'
    #pattern = 'd'
    b_m = algo.BoyerMoore(text, pattern)
    b_m.search()
    print(b_m.results.time, b_m.results.n_operations)


if __name__ == '__main__':
    main()