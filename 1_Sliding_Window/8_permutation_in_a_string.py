str = "bcdxabcdy"
pattern = "bcdyabcdx"
pattern_freq = {}
str_freq = {}
for window_end in range(len(pattern)):
    right_char = pattern[window_end]
    if right_char not in pattern_freq:
        pattern_freq[right_char] = 0
    pattern_freq[right_char] += 1
ref_pattern_freq = pattern_freq

for window_end in range(len(str)):
    if str[window_end] in pattern_freq:
        if str[window_end] not in str_freq:
            str_freq[str[window_end]] = 0
        str_freq[str[window_end]] += 1
        print("str_freq",str_freq)
    if str_freq == pattern_freq:
        print(True)
    if str[window_end] not in pattern_freq:
        str_freq = {}

#time complexity O(N+M) N: number of characters in string M:number of char in pattern
#space complexity O(M) in the worst case, the whole pattern can have distinct char
