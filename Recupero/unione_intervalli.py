def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    result: list[list[int]] = []
    intervals = sorted(intervals, key = lambda x: x[0])
    i = 0
    
    while i < len(intervals) -1:
        a: int = intervals[i][0]
        b: int = intervals[i][1]
        c: int = intervals[i+1][0]
        d: int = intervals[i+1][1]
        if a <= b and c <= d and b >= c:
            intervals[i+1] = [a, d]
            intervals[i] = []
        i += 1
    return [x for x in intervals if x != []]