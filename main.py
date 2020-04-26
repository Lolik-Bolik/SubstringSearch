import algorithms as algo
import argparse
import os
import csv
import pandas as pd


def main(args):
    with open('statistic.csv', 'w') as file:
        fnames = ['Method_name', 'Work_time', 'Operations_amount']
        writer = csv.DictWriter(file, fieldnames=fnames)
        writer.writeheader()
        reference_names = ['bad_t_1.txt', 'bad_t_2.txt', 'bad_t_3.txt', 'bad_t_4.txt',
                           'good_t_1.txt', 'good_t_2.txt', 'good_t_3.txt', 'good_t_4.txt']
        target_names = ['bad_w_1.txt', 'bad_w_2.txt', 'bad_w_3.txt', 'bad_w_4.txt',
                        'good_w_1.txt', 'good_w_2.txt', 'good_w_3.txt', 'good_w_4.txt']
        for reference, target in zip(reference_names, target_names):
            with open(os.path.join(args.path, reference)) as text_file:
                text = text_file.read()
            with open(os.path.join(args.path, target)) as pattern_file:
                pattern = pattern_file.read()
            boyer = algo.BoyerMoore(text, pattern)
            results = boyer.search()
            # print(results.time, results.n_operations)
            writer.writerow({'Method_name': boyer.__class__.__name__, 'Work_time': results.time,
                            'Operations_amount': results.n_operations})


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str,
                        default='/home/alexslav/HSE_STUFF/Burashnikov/SubstringSearch/benchmarks',
                        help='path to benchmarks files')
    args = parser.parse_args()
    main(args)