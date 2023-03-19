from time_compexity_plot.plot import plot_time_complexity


def remove_element(nums: list[int], val: int) -> int:
    cur = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[cur] = nums[i]
            cur += 1
    return cur


if __name__ == '__main__':
    plot_time_complexity(lambda n: remove_element([1, 2, 3] * (n // 3), 2))
