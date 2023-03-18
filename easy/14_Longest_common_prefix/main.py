def longest_common_prefix(strs: list[str]) -> str:
    ans = ""
    strs = sorted(strs)
    for i in range(len(strs[0])):
        if strs[0][i] != strs[-1][i]:
            return ans
        ans += strs[0][i]
    return ans


def plot_time_complexity():
    import numpy as np
    from timeit import timeit
    import matplotlib.pyplot as plt
    from tqdm import tqdm
    ns = np.arange(10 ** 3, 10 ** 7, 10 ** 5)
    times = lambda n: timeit(lambda: longest_common_prefix(
        [
            "asdfgh"*(n//6),
            "asdfgh"*(n//6),
            "asdfgh"*(n//6),
        ]
    ), number=1)
    fig = plt.plot(ns, list(map(times, tqdm(ns))))
    plt.savefig("complexity.png")
    plt.show()


if __name__ == '__main__':
    # print(longest_common_prefix(["asd", "asdsfa", "a"]))
    plot_time_complexity()