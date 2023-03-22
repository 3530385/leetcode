from time_compexity_plot.plot import plot_time_complexity


def bin_search(nums, target, left=0, right=None):
    if right is None:
        right = len(nums) - 1
    if left == right - 1:
        if target <= nums[left]:
            return left
        elif nums[left] < target <= nums[right]:
            return right
        return right + 1
    mid = (left + right) // 2
    if target == nums[mid]:
        return mid
    if target < nums[mid]:
        return bin_search(nums, target, left, mid)
    else:
        return bin_search(nums, target, mid, right)


def search_insert(nums: list[int], target: int):
    if len(nums) == 1:
        return 0 if target <= nums[0] else 1
    if nums:
        return bin_search(nums, target)
    return 0


if __name__ == '__main__':
    plot_time_complexity(lambda inputs: search_insert(inputs, 99), lambda n: list(range(n)), n_start=100,
                         n_stop=int(0.7 * 10 ** 6), min_of_n=100)
