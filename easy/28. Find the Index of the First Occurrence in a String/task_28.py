from time_compexity_plot.plot import plot_time_complexity


def sub_idx(haystack: str, needle: str) -> int:
    return haystack.find(needle)


if __name__ == '__main__':
    plot_time_complexity(lambda n: sub_idx(haystack="abcdef" * (n // 6) + "sad", needle="sad"))
