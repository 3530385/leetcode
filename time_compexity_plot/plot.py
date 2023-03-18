from timeit import timeit
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np


def plot_time_complexity(func: callable, n_start: int = 10 ** 3, n_stop: int = 10 ** 6,
                         n_step: int = 10 ** 3, n_times: int = 1) -> object:
    ns = np.arange(n_start, n_stop, n_step)
    times = lambda n: timeit(lambda: func(n),
                             number=n_times)
    plt.plot(ns, list(map(times, tqdm(ns))))
    plt.xlabel("n")
    plt.ylabel("time, s")
    plt.savefig("complexity.png")
    plt.show()
