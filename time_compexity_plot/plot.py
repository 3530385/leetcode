from timeit import timeit
from typing import Union

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


def get_measure_time_func(func: callable, min_of_n, n_times) -> callable:
    return lambda inputs: min([timeit(lambda: func(inputs),
                                      number=n_times) for _ in range(min_of_n)])


def plot_time_complexity(funcs: Union[list[callable], callable], inputs_func: callable, n_start: int = 10 ** 3,
                         n_stop: int = 10 ** 6,
                         n_step: int = 10 ** 3, n_times: int = 1, min_of_n=2):
    ns = list(np.arange(n_start, n_stop, n_step))
    if isinstance(funcs, list):
        pass
    elif isinstance(funcs, callable):
        func = funcs
        funcs = [0]
        funcs[0] = func
    for func in funcs:
        inputs_gen = (inputs_func(n) for n in np.arange(n_start, n_stop, n_step))
        times = get_measure_time_func(func, min_of_n, n_times)
        plt.plot(ns, list(map(times,
                              tqdm(inputs_gen,
                                   total=(n_stop - n_start) // n_step))),
                 label=func.__name__)
    plt.xlabel("n")
    plt.ylabel("time, s")
    plt.legend()
    plt.savefig("complexity.png")
    plt.show()


if __name__ == '__main__':
    plot_time_complexity(lambda inputs: inputs[5], lambda n: [3, 2, 1] * n, n_times=1, min_of_n=20)
