from timeit import timeit

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


def plot_time_complexity(func: callable, inputs_func: callable, n_start: int = 10 ** 3, n_stop: int = 10 ** 6,
                         n_step: int = 10 ** 3, n_times: int = 1, min_of_n = 2):
    ns = np.arange(n_start, n_stop, n_step)
    inputs_gen = (inputs_func(n) for n in np.arange(n_start, n_stop, n_step))
    times = lambda inputs: min([timeit(lambda: func(inputs),
                                  number=n_times) for _ in range(min_of_n)])
    plt.plot(ns, list(map(times, tqdm(inputs_gen, total=(n_stop-n_start)//n_step))))
    plt.xlabel("n")
    plt.ylabel("time, s")
    plt.savefig("complexity.png")
    plt.show()


if __name__ == '__main__':
    plot_time_complexity(lambda inputs: inputs[5], lambda n: [3, 2, 1] * n, n_times=1, min_of_n=20)
