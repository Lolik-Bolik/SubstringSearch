import algorithms as algo
import argparse
import os
import csv
import pandas as pd

def main(args):

    with open('statistic.csv', 'w') as file:
        columns_names = ['Method_name', 'Average_Work_time', 'Operations_amount']
        writer = csv.DictWriter(file, fieldnames=columns_names)
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
            algorithms = [(name, f(text, pattern)) for name, f in algo.__dict__.items() if callable(f)]
            for name, algorithm in algorithms:
                average_time = 0
                for exp_number in range(args.experiment_number):
                    results = algorithm.search()
                average_time += results.time
                average_time = average_time / args.experiment_number
                writer.writerow({'Method_name': name, 'Average_Work_time': average_time,
                                'Operations_amount': results.n_operations})



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str,
                        default='./benchmarks',
                        help='path to benchmarks files')
    parser.add_argument('-exp_n', '--experiment_number', type=int,
                        default=5,
                        help='number of experiments')
    args = parser.parse_args()
    main(args)