str = "ppqp"
pattern = "pq"
char_frequency = {}
window_start = 0
matched = 0

for window_end in range(len(pattern)):
    right_char = pattern[window_end]
    if right_char not in char_frequency:
        char_frequency[right_char] = 0
    char_frequency[right_char] += 1

for window_end in range(len(str)):
    if window_end > len(pattern) - 1:
        if str[window_start] in char_frequency:
            if char_frequency[str[window_start]] == 0:
                matched -= 1
            char_frequency[str[window_start]] += 1
        window_start += 1

    if str[window_end] in char_frequency:
        char_frequency[str[window_end]] -= 1
        if char_frequency[str[window_end]] == 0:
            matched += 1

    if matched == len(char_frequency):
        print([window_start,window_end])
        
#time complexity O(N+M)
#space complexity O(M) M -> hashmap for char_frequency
