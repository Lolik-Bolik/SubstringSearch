import algorithms as algo
import argparse
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import random


def draw_statistic(statistic):
    figure = plt.figure(1, (15, 15))
    # colors =
    for object in statistic.Method_name.unique():
        method = statistic[statistic['Method_name'] == object]
        plt.plot(method['File_length'], method['Average_Work_time'], )

    plt.show()


def main(args):
    if args.make_csv:
        with open('statistic.csv', 'w') as file:
            columns_names = ['File_name', 'Method_name', 'Average_Work_time', 'Operations_amount', 'File_length']
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
                    writer.writerow({'File_name': reference, 'Method_name': name, 'Average_Work_time': round(average_time, 4),
                                     'Operations_amount': results.n_operations, 'File_length': len(text)})

    statistics = pd.read_csv('statistic.csv')
    good_statistic = statistics[16:]
    bad_statistic = statistics[:15]
    draw_statistic(good_statistic)
    draw_statistic(bad_statistic)



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str,
                        default='./benchmarks',
                        help='path to benchmarks files')
    parser.add_argument('-exp_n', '--experiment_number', type=int,
                        default=5,
                        help='number of experiments')
    parser.add_argument('-make_csv', type=bool,
                        default=False)
    args = parser.parse_args()
    main(args)