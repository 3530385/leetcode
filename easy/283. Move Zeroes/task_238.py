from time_compexity_plot.plot import plot_time_complexity


def move_zeroes(nums: list[int]) -> None:
    non_zero_index = 0
    for i, value in enumerate(nums):
        if value:
            nums[non_zero_index], nums[i] = value, nums[non_zero_index]
            non_zero_index += 1


if __name__ == "__main__":
    nums = [1, 0, 3, 4]
    move_zeroes(nums)
    assert nums == [1, 3, 4, 0], f"{nums=}"
    plot_time_complexity(move_zeroes,
                         lambda n: ([3, 0, 0, 4, 5] * (n // 5),))
