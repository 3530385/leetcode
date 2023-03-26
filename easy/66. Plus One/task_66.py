from time_compexity_plot.plot import plot_time_complexity


def plus_one(digits: list) -> list:
    idx = -1
    n = len(digits)
    while digits[idx] == 9 and idx != -n:
        digits[idx] = 0
        idx -= 1
    if digits[idx] != 9:
        digits[idx] += 1
        return digits
    if digits[0] == 9:
        digits[0] = 1
        digits.append(0)
    return digits


def list_to_int_plus_one(digits: list[int]) -> list[int]:
    res = int("".join(map(str, digits)))
    res += 1
    return list(map(int, str(res)))


if __name__ == '__main__':
    plot_time_complexity([plus_one, list_to_int_plus_one],
                         lambda n: [9] * n,
                         min_of_n=20, n_stop=10**5)
