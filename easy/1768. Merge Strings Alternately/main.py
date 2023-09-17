from itertools import zip_longest
from time_compexity_plot.plot import plot_time_complexity


def get_input():
    word1 = input()
    word2 = input()
    return word1, word2


def simple_solution(word1: str, word2: str) -> str:
    result = ""
    for char1, char2 in zip_longest(word1, word2, fillvalue=""):
        result += char1 + char2
    return result


def one_line_solution(word1: str, word2: str) -> str:
    return ''.join(chars[0] + chars[1]
                   for chars in zip_longest(word1, word2, fillvalue=''))


def main():
    word1, word2 = get_input()
    return one_line_solution(word1, word2)


if __name__ == "__main__":
    plot_time_complexity([one_line_solution, simple_solution],
                         lambda n: ("010" * (n // 6), "101" * (n // 6)),
                         n_stop=10 ** 5)
