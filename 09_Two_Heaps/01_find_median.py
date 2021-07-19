from heapq import *


class MedianOfAStream:

    maxHeap = []
    minHeap = []

    def insert_num(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def find_median(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]/1.0


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))


main()

# time complexity: O(logN) insertion in the heap
# space complexity: O(N) storing all the numbers
