def roman_to_int(s: str) -> int:
    sym_to_value = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = 0
    for current_char, next_char in zip(s, s[1:]):
        if sym_to_value[current_char] < sym_to_value[next_char]:
            result -= sym_to_value[current_char]
        else:
            result += sym_to_value[current_char]
    result += sym_to_value[s[-1]]
    return result


def faster_solutions(s: str) -> int:
    roman_to_integer = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    s = s.replace("IV", "IIII") \
        .replace("IX", "VIIII") \
        .replace("XL", "XXXX") \
        .replace("XC", "LXXXX") \
        .replace("CD", "CCCC").replace("CM", "DCCCC")
    return sum(map(lambda x: roman_to_integer[x], s))


def plot_time_complexity():
    import numpy as np
    from timeit import timeit
    import matplotlib.pyplot as plt
    from tqdm import tqdm
    ns = np.arange(10 ** 3, 10 ** 6, 10 ** 4)
    times = lambda n: timeit(lambda: roman_to_int(
        "X" * n
    ), number=3)
    plt.plot(ns, list(map(times, tqdm(ns))))
    plt.savefig("complexity.png")
    plt.show()


if __name__ == '__main__':
    # print(roman_to_int("III"))
    plot_time_complexity()