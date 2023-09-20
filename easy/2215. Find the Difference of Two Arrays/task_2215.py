from time_compexity_plot.plot import plot_time_complexity

def find_difference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)
    return [list(set_nums1 - set_nums2), list(set_nums2-set_nums1)]

if __name__ =="__main__":
    assert find_difference([1,2,3], [3,2,2,2,2,5,4]) == [[1], [4, 5]],   find_difference([1,2,3], [3,2,2,2,2,5,4]) 
    plot_time_complexity([find_difference],
                         lambda n: ([1,2,3]*(n//3),[5,2,3]*(n//3)))
