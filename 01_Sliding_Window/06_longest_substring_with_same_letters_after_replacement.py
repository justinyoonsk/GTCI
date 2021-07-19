str = "abccde"
k = 1
char_freq = {}
window_start = 0
max_substring = float("-inf")
for window_end in range(len(str)):
    right_str = str[window_end]
    if right_str not in char_freq:
        char_freq[right_str] = 0
    char_freq[right_str] += 1

    while len(char_freq) > 2:
        char_freq[str[window_start]] -= 1
        if char_freq[str[window_start]] == 0:
            del char_freq[str[window_start]]
        window_start += 1

    max_substring = max(max_substring, min(min(char_freq.values()), k)
                        + max(char_freq.values()))
print(max_substring)
#time complexity O(N)
#space complexity O(1)
