s = 8
arr = [3,4,1,1,6]
window_sum = 0
window_start = 0
min_length = float("inf")
for window_end in range(len(arr)):
    window_sum += arr[window_end]
    while window_sum >= s:
        min_length = min(min_length, window_end - window_start + 1)
        window_sum -= arr[window_start]
        window_start += 1
    if min_length == float("inf"):
        print(0)
print(min_length)

#time complexity O(n)
#space complexity O(1)
