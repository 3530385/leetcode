from time_compexity_plot.plot import plot_time_complexity


def length_of_last_world(string: str) -> int:
    return len(string.split()[-1])


def length_of_last_world_with_pop(string: str) -> int:
    return len(string.split().pop())


def length_of_last_world_backprop(string: str) -> int:
    ans = 0
    end = -1
    while string[end] == " ":
        end -= 1
    try:
        while string[end] != " ":
            ans += 1
            end -= 1
    finally:
        return ans


if __name__ == '__main__':
    plot_time_complexity([
        length_of_last_world,
        length_of_last_world_with_pop,
        length_of_last_world_backprop,
    ],
        lambda n: "  word  word " * (n // 13),
        n_start=20, n_stop=10 ** 7, n_step=10 ** 5, min_of_n=10)
