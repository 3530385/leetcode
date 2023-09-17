import pathlib
from timeit import timeit
from typing import Union, Callable

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm


def get_measure_time_func(func: Callable, min_of_n, n_times) -> Callable:
    return lambda inputs: min([
        timeit(lambda: func(*inputs),
               number=n_times) for _ in range(min_of_n)])


def save_readme(fig_name: str):
    if pathlib.Path(fig_name).exists():
        with open("README.md", "w") as f:
            f.write(f"""# Time complexity plot\n![image]({fig_name})""")
    else:
        raise FileExistsError(f"{fig_name} file does not exists")


def plot_time_complexity(funcs: Union[list[Callable], Callable],
                         inputs_func: Callable,
                         n_start: int = 10 ** 3,
                         n_stop: int = 10 ** 6,
                         n_step: int = 10 ** 3,
                         n_times: int = 1,
                         min_of_n: int = 2,
                         generate_readme: bool = True,
                         fig_name: str = "complexity.png"):
    """
    :param funcs:
        Список функций или одна функция, сложность которой необходимо измерить
    :param inputs_func:
        Функция, которая создаёт inputs для тестируемых функций.
        Она обязательно должна принимать число n в качестве аргумента.
        Пример:
            lambda n: [0] * n,
    :param n_start:
        Количество данных с которого начать оценку сложности
    :paam n_stop:
        Количество данных которым окончить оценку сложности
    :param n_step:
        Количество шагов между n_start и n_step
    :param n_times:
    :param min_of_n:
    :param generate_readme:
    :param fig_name:
    :return:
    """
    ns = list(np.arange(n_start, n_stop, n_step))
    if isinstance(funcs, list):
        pass
    elif isinstance(funcs, Callable):
        funcs = [funcs]
    for func in funcs:
        inputs_gen = (inputs_func(n)
                      for n in np.arange(n_start, n_stop, n_step))
        times = get_measure_time_func(func, min_of_n, n_times)
        plt.plot(ns, list(map(times,
                              tqdm(inputs_gen,
                                   total=(n_stop - n_start) // n_step))),
                 label=func.__name__)
    plt.xlabel("n")
    plt.ylabel("time, s")
    plt.legend()
    plt.savefig(fig_name)
    plt.show()
    if generate_readme:
        save_readme(fig_name)


if __name__ == '__main__':
    plot_time_complexity(lambda inputs: inputs[5],
                         lambda n: [3, 2, 1] * n,
                         n_times=1,
                         min_of_n=20)
