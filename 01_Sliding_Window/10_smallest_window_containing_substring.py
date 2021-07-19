s = "abdbca"
t = "abc"
char_freq = {}
matched = 0
min_length = float("inf")
window_start = 0
answer = ""
for char in range(len(t)):
    right_char = t[char]
    if t[char] not in char_freq:
        char_freq[t[char]] = 0
    char_freq[t[char]] += 1

for window_end in range(len(s)):
    if s[window_end] in char_freq:
        char_freq[s[window_end]] -= 1
        if char_freq[s[window_end]] >= 0:
            matched += 1
    while matched == len(t):
        if min_length > window_end - window_start + 1:
            min_length = window_end - window_start + 1
            answer = s[window_start:window_end + 1]
        if s[window_start] in char_freq:
            char_freq[s[window_start]] += 1
            if char_freq[s[window_start]] > 0:
                matched -= 1

        window_start += 1

print(answer)
#time complexity O(N+M) iterating through string and iterating through pattern
#space complexity O(M) distinct characters in hashmap, worst case we need O(N)
#when the input string is a permutation of the pattern
