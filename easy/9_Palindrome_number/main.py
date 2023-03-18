def read() -> int:
    return int(input())


def is_palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def main():
    n = read()
    print(is_palindrome(n))


def plot_time_complexity():
    import numpy as np
    from timeit import timeit
    import matplotlib.pyplot as plt
    ns = (np.arange(10 ** 3, 10 ** 8, 10 ** 3))
    times = lambda n: timeit(lambda: is_palindrome(
        int("1" * n)), number=3)
    plt.plot(ns, list(map(times, ns)))
    plt.xlabel("n")
    plt.ylabel("time, s")
    plt.savefig("complexity.png")
    plt.show()


if __name__ == '__main__':
    plot_time_complexity()
