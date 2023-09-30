from timeit import timeit
import numpy as np
import matplotlib.pyplot as plt


def is_valid(s: str) -> bool:
    open_to_close = dict(("()", "[]", "{}"))
    stack = []
    for char in s:
        if char in "[{(":
            stack.append(char)
        elif not stack or char != open_to_close[stack.pop()]:
            return False
    return len(stack) == 0


def plot_time_complexity():
    ns = np.arange(10**3, 10**6, 10**3)
    times = lambda n: timeit(
        lambda: is_valid("(" * (n // 2) + ")" * (n // 2)), number=3
    )
    plt.plot(ns, list(map(times, ns)))
    plt.xlabel("n")
    plt.ylabel("time, s")
    plt.savefig("complexity.png")
    plt.show()


if __name__ == "__main__":
    plot_time_complexity()
