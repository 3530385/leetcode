"""
module docstring
"""


def move_zeroes(nums: list[int]) -> None:
    """
    docstring
    """
    non_zero_index = 0
    for i, value in enumerate(nums):
        if value:
            nums[non_zero_index], nums[i] = value, nums[non_zero_index]
            non_zero_index += 1


if __name__ == "__main__":
    numbers = [1, 0, 3, 4]
    move_zeroes(numbers)
    assert numbers == [1, 3, 4, 0], f"{numbers=}"
    print("Done!")
    # plot_time_complexity(move_zeroes, lambda n: ([3, 0, 0, 4, 5] * (n // 5),))
