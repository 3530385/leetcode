import statistics as st

from time_compexity_plot.plot import plot_time_complexity


def find_max_subarray(nums: list, k: int):
    current_mean = st.mean(nums[:k])
    max_mean = current_mean
    for i in range(len(nums) - k):
        current_mean = current_mean + (nums[i+k] - nums[i])/k
        if current_mean > max_mean:
            max_mean = current_mean
    return max_mean

if __name__ == "__main__":
    assert find_max_subarray( [1,12,-5,-6,50,3], 4) == 12.75000
    plot_time_complexity([find_max_subarray],
                         lambda n: ([1,2,3]*(n//3), 4))
