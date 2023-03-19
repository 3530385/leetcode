from time_compexity_plot.plot import plot_time_complexity


def remove_duplicates(nums: list[int]) -> int:
    cur = 0
    for i in range(1, len(nums)):
        if nums[i - 1] != nums[i]:
            nums[cur + 1] = nums[i]
            cur += 1
    return cur + 1


if __name__ == '__main__':
    plot_time_complexity(lambda n: remove_duplicates(list(range(n))))
