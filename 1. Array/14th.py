# https://leetcode.com/problems/merge-intervals/

def merge(intervals):

    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If the list of merged intervals is empty or if the current interval does not overlap with the previous, simply append it
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)

        else:
            #Otherwise there is overlap, so we merge the current and previous intervals

            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

intervals = [[1,3],[2,6],[8,10],[10,18]]
print(merge(intervals))