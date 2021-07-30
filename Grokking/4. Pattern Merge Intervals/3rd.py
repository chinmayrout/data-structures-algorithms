def merge(interval_a, interval_b):
    result = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(interval_a) and j < len(interval_b):
        # Check if intervals overlap and intervals_a[i]'s start time lies within the other interval_b[j]
        a_overlaps_b = interval_a[i][start] >= interval_b[j][start] and \
            interval_a[i][start] <= interval_b[j][end]

        # Check if intervals overlap and interval_a[j]'s start time lies within the other interval_b[i]
        b_overlaps_a = interval_b[j][start] >= interval_a[i][start] and \
            interval_b[j][start] <= interval_a[i][end]


        # Store the intersection part
        if (a_overlaps_b or b_overlaps_a):
            result.append([max(interval_a[i][start], interval_b[j][start]), min(
                interval_a[i][end], interval_b[j][end])])

        # Move next from the interval which is finishing first
        if interval_a[i][end] < interval_b[j][end]:
            i += 1
        else:
            j += 1

    return result



def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()