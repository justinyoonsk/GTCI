arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k = 2
window_start = 0
zero_counter = 0
ones_freq = {}
max_subarray = float("-inf")
for window_end in range(len(arr)):
    if arr[window_end] == 0:
        zero_counter += 1
    while zero_counter > k:
        if arr[window_start] == 0:
            zero_counter -= 1
        window_start += 1

    print("end",window_end)
    print("start",window_start)

    max_subarray = max(max_subarray, window_end - window_start + 1)
print(max_subarray)

#time complexity O(N)
#space complexity O(1)
