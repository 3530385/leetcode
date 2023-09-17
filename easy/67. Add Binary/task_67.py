from itertools import zip_longest

from time_compexity_plot.plot import plot_time_complexity


def add_binary(a: str, b: str) -> str:
    return str(bin(int(a, 2) + int(b, 2)))[2:]


def add_binary_my_slow(a: str, b: str):
    p = 0
    r = ''
    for i, j in zip_longest(a[::-1], b[::-1], fillvalue="0"):
        p, m = divmod(int(i) + int(j) + p, 2)
        r = str(m) + r
    if p:
        r = str(p) + r
    return r


def add_binary_my_faster(a: str, b: str):
    p = 0
    r = ''
    min_len = min(len(a), len(b))
    for i in range(-min_len, -1):
        p, m = divmod(int(a[i]) + int(b[i]) + p, 2)
        r += str(m)
    if p:
        r += str(p)
    r = a[:len(a)-min_len] + r
    return r


if __name__ == "__main__":
    plot_time_complexity([add_binary, add_binary_my_faster, add_binary_my_slow],
                         lambda n: ("010" * (n // 3), "101" * (n // 3)), n_stop=10 ** 5)
    print(add_binary_my_faster("10011", "1101"))
    print(add_binary("10011", "1101"))