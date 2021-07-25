from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
def find_next_interval(intervals):
    n = len(intervals)

    maxStartHeap, maxEndHeap = [], []

    result = [0 for x in range(n)]

    for endIndex in range(n):
        heappush(maxStartHeap, (-intervals[endIndex].start, endIndex))
        heappush(maxEndHeap, (-intervals[endIndex].end, endIndex))
    print(maxStartHeap)
    # maxStartHeap = [(-5, 2), (-2, 0), (-3, 1)]
    # maxEndHeap = [(-6, 2), (-3, 0), (-4, 1)]
    for _ in range(n):
        topEnd, endIndex = heappop(maxEndHeap)
        result[endIndex] = -1
        if -maxStartHeap[0][0] >= -topEnd:
            topStart, startIndex = heappop(maxStartHeap)
            while maxStartHeap and -maxStartHeap[0][0] >= -topEnd:
                topStart, startIndex = heappop(maxStartHeap)
            result[endIndex] = startIndex

            heappush(maxStartHeap, (topStart, startIndex))
    return result




def main():
    result = find_next_interval([Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

main()

# time complexity: O(NLogN), where N is the total number of intervals
# space complexity: O(N), storing all intervals in the heaps
