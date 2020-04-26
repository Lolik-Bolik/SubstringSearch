import algorithms as algo
import os


def main():
    reference_names = ['bad_t_1.txt', 'bad_t_2.txt', 'bad_t_3.txt', 'bad_t_4.txt',
                       'good_t_1.txt', 'good_t_2.txt', 'good_t_3.txt', 'good_t_4.txt']
    target_names = ['bad_w_1.txt', 'bad_w_2.txt', 'bad_w_3.txt', 'bad_w_4.txt',
                    'good_w_1.txt', 'good_w_2.txt', 'good_w_3.txt', 'good_w_4.txt']
    for reference, target in zip(reference_names, target_names):
        with open(os.path.join('./benchmarks', reference)) as text_file:
            text = text_file.read()
        with open(os.path.join('./benchmarks', target)) as pattern_file:
            pattern = pattern_file.read()
        boyer = algo.KarpRabin(text, pattern)
        results = boyer.search(True)
        print(results)
    #text = 'fdvddasdadvdgdvd'
    #pattern = 'dvd'


if __name__ == '__main__':
    main()