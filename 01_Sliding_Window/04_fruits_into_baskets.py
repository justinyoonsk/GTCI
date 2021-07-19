fruits = ["A","B","C","B","B","C"]
fruit_freq = {}
window_start = 0
max_fruits = float("-inf")
for window_end in range(len(fruits)):
    if fruits[window_end] not in fruit_freq:
        fruit_freq[fruits[window_end]] = 0
    fruit_freq[fruits[window_end]] += 1

    while len(fruit_freq) > 2:
        fruit_freq[fruits[window_start]] -= 1
        if fruit_freq[fruits[window_start]] == 0:
            del fruit_freq[fruits[window_start]]
        window_start += 1
    max_fruits = max(max_fruits, window_end - window_start + 1)
print(max_fruits)

#time complexity O(N)
#space complexity O(1)
