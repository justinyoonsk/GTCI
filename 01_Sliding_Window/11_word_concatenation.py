str = "catfoxcat"
words = ["cat","fox"]
len_words = len(words[0])
answer = []
word_freq = {}
matched = 0
window_start = 0
for i in range(len(words)):
    if words[i] not in word_freq:
        word_freq[words[i]] = 0
    word_freq[words[i]] += 1

for window_end in range(0,len(str),len_words):
    word = str[window_end:window_end+len_words]
    if word in word_freq:
        word_freq[word] -= 1
        if word_freq[word] >= 0:
            matched += 1
        if word_freq[word] < 0:
            window_start += len_words
        while matched == len(words):
            if str[window_start:window_start+len_words] in word_freq:
                word_freq[str[window_start:window_start+len_words]] += 1
                if word_freq[str[window_start:window_start+len_words]] > 0:
                    matched -= 1
                    answer.append(window_start)
            window_start += len_words
print(answer)

#time complexity O(N + M)

