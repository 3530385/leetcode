from time_compexity_plot.plot import plot_time_complexity


def largest_altitude(gain: list[int]) -> int:
    result = 0
    current_altitude = 0
    for diff in gain:
        current_altitude += diff
        result = max(result, current_altitude)
    return result



if __name__ == "__main__":
    assert largest_altitude([-5, 1, 5, 0, -7]) == 1
    plot_time_complexity([largest_altitude],
                         lambda n: ([1,2,3]*(n//3),))
