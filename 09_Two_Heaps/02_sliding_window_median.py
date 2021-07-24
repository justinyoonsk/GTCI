from heapq import *
import heapq

class SlidingWindowMedian:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def find_sliding_window_median(self, nums, k):
        result = [0.0 for x in range(len(nums) - k + 1)]
        for i in range(0, len(nums)):
            if not self.maxHeap or nums[i] <= -self.maxHeap[0]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])
            self.rebalance_heaps()

            if i - k + 1 >= 0:
                if len(self.maxHeap) == len(self.minHeap):
                    result[i - k + 1] = -self.maxHeap[0] / 2.0 + self.minHeap[0] / 2.0
                else:
                    result[i - k + 1] = -self.maxHeap[0] / 1.0
                elementToBeRemoved = nums[i - k + 1]
                if elementToBeRemoved <= -self.maxHeap[0]:
                    self.remove(self.maxHeap, -elementToBeRemoved)
                else:
                    self.remove(self.minHeap, elementToBeRemoved)
                self.rebalance_heaps()

        return result

    def remove(self, heap, element):
        ind = heap.index(element)
        heap[ind] = heap[-1]
        del heap[-1]



        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)


    def rebalance_heaps(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median([1, 2, -1, 3, 5], 2)

    print("Sliding window medians are: " + str(result))

main()

#time complexity: O(N*K) N: total number of elements, K: size of the sliding window
# inserting/removing numbers from heaps of size K: O(logK)
# removing element going out the sliding window will take O(K)
#space complexity: O(K): storing numbers in sliding window
