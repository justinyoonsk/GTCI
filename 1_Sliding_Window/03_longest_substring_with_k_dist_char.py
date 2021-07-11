str = "cbbebi"
K = 3
char_frequency = {}
window_start = 0
max_value = float("-inf")
for window_end in range(len(str)):
    if str[window_end] not in char_frequency:
        char_frequency[str[window_end]] = 0
    char_frequency[str[window_end]] += 1

    while len(char_frequency) > K and window_start < window_end:
        char_frequency[str[window_start]] -= 1
        if char_frequency[str[window_start]] == 0:
            del char_frequency[str[window_start]]
        window_start += 1
    max_value = max(max_value, window_end - window_start + 1)
print(max_value)

#time complexity = O(N)
#space complexity = O(K) hashmap 
