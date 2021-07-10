str = "abccde"
char_freq = {}
window_start = 0
max_substring = float("-inf")
for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in char_freq:
        char_freq[right_char] = 0
    char_freq[right_char] += 1
    while char_freq[right_char] == 2:
        char_freq[str[window_start]] -= 1
        window_start += 1

    max_substring = max(max_substring, window_end - window_start + 1)
print(max_substring)

#time complexity O(N)
#space complexity O(K) hashmap but could say O(1) because there are 26 english letters
