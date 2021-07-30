# Given a list of appointments, find all the conflicting appointments.

def find_conflicting_appointment(intervals):
    result = []
    intervals.sort(key=lambda x: x[0])

    start, end = 0, 1
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i-1][end]:
            print([intervals[i - 1], intervals[i]])

    return result


Appointments = [[4,5], [2,3], [3,6], [5,7], [7,8]]
print(find_conflicting_appointment(Appointments))
