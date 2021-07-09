#GTCI Maximum Sum Subarray of Size K (easy)
k = 3
arr = [2, 1, 5, 1, 3, 2]
result = []
window_sum = 0.0
max_sum = float("-inf")
window_start = 0
for window_end in range(len(arr)):
    window_sum += arr[window_end]
    if window_end >= k - 1:
        max_sum = max(max_sum, window_sum)
        window_sum -= arr[window_start]
        window_start += 1
print(max_sum)

#time complexity O(N)
#space complexity O(1)
