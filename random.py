'''

from collections import deque
arr = [2, 5, 3, 10]
target = 30
product = 1
left = 0
answer = []
for right in range(len(arr)):
    product *= arr[right]
    while product >= target:
        product /= arr[left]
        left += 1
    temp_list = deque()
    for i in range(right, left-1, -1):
        temp_list.appendleft(arr[i])
        answer.append(list(temp_list))
print(answer)
//
'''

'''
arr = [-1, 1, 2, 3, 4]
target = 5
arr = sorted(arr)
#[-1, 1, 2, 3, 4]
counter = 0
for i in range(len(arr) - 2):
    left = i + 1
    right = len(arr) - 1
    target_sum = target - arr[i]
    while left < right:
        if arr[left] + arr[right] < target_sum:
            print(arr[i], arr[left], arr[right])
            counter += right - left
            left += 1
        else:
            right -= 1
print(counter)
'''
'''
arr = [-2, 0, 1, 2, 3, 5]
target_sum = 2
smallest_diff = float("inf")
answer = 0
arr = sorted(arr)
for i in range(len(arr)-2):
    left = i + 1
    right = len(arr) - 1
    while left < right:
        target_diff = target_sum - arr[i] - arr[left] - arr[right]
        if target_diff == 0:
            print("done, answer:", target_sum - target_diff)
        if abs(target_diff) < abs(smallest_diff):
            smallest_diff = target_diff
        if target_diff > 0:
            left += 1
        else:
            right -= 1

print(target_sum - smallest_diff)
'''
'''
arr = [-3, 0, 1, 2, -1, 1, -2]
arr = sorted(arr) #[-3, -2, -1, 0, 1, 1, 2]
ans = []
for i in range(len(arr)):
    target_sum = -arr[i]
    left = i + 1
    right = len(arr) - 1

    while left < right:
        if arr[left] == arr[left-1]:
            break
        if arr[left] + arr[right] < target_sum:
            left += 1
        if arr[left] + arr[right] > target_sum:
            right -= 1
        if arr[left] + arr[right] == target_sum:
            ans.append([-target_sum, arr[left], arr[right]])
            left += 1
print(ans)
'''
'''
arr = [-3, -1, 0, 1, 2]
arr_copy = [0 for x in range(len(arr))]
highestIndex = len(arr) - 1
left = 0
right = len(arr) - 1
while left <= right:
    squaresLeft = arr[left] * arr[left]
    squaresRight = arr[right] * arr[right]
    if squaresRight > squaresLeft:
        arr_copy[highestIndex] = squaresRight
        highestIndex -= 1
        right -= 1
    else:
        arr_copy[highestIndex] = squaresLeft
        highestIndex -= 1
        left += 1
print(arr_copy)
'''
'''
arr = [3, 2, 3, 6, 3, 10, 9, 3]
key = 3
#output = 4 [2, 6, 10, 9]
nextElement = 0
for i in range(len(arr)):
    if arr[i] != key:
        arr[nextElement] = arr[i]
        nextElement += 1
print(nextElement)
'''
'''
arr = [2, 3, 3, 3, 6, 9, 9]
next_non_duplicate = 1
i = 1
while(i < len(arr)):
    if arr[next_non_duplicate - 1] != arr[i]:
        arr[next_non_duplicate] = arr[i]
        next_non_duplicate += 1
        print(next_non_duplicate)
    i += 1

print(next_non_duplicate)
'''
'''
arr = [2, 3, 3, 3, 6, 9, 9]
#arr = [2, 3, 3, 3, 6, 9]
left = 0
right = len(arr) - 1
while(left <= right):
    if arr[left] == arr[left + 1]:
        del arr[left]
        right -= 1
    left += 1
    if arr[right] == arr[right - 1]:
        del arr[right]
        right -= 1
    right -= 1
print(len(arr))
'''
'''
arr = [1, 2, 3, 4, 6]
target_sum = 6
left = 0
right = len(arr) - 1
while(left < right):
    current_sum = arr[left] + arr[right]
    if current_sum == target_sum:
        print([left, right])
    if target_sum > current_sum:
        left += 1
    else:
        right -= 1
'''
'''
#Two Pointers mine
arr = [2, 5, 9, 11]
target_sum = 11
left = 0
right = len(arr) - 1

for i in range(len(arr)):
    if arr[left] + arr[right] > target_sum:
        right -= 1
    if arr[left] + arr[right] < target_sum:
        left += 1
    if arr[left] + arr[right] == target_sum:
        print([left, right])
    else:
        print([])
'''
'''
str1 = "catcatfoxfox"
words = ["cat", "fox"]

if len(words) == 0 or len(words[0]) == 0:
    print([])

word_frequency = {}

for word in words:
    if word not in word_frequency:
        word_frequency[word] = 0
    word_frequency[word] += 1

result_indices = []
words_count = len(words)
word_length = len(words[0])

for i in range((len(str1) - words_count * word_length) + 1):
    words_seen = {}
    for j in range(0, words_count):
        next_word_index = i + j * word_length
        word = str1[next_word_index: next_word_index + word_length]
        if word not in word_frequency:
            break
        if word not in words_seen:
            words_seen[word] = 0
        words_seen[word] += 1

        if words_seen[word] > word_frequency.get(word, 0):
            break

        if j + 1 == words_count:
            result_indices.append(i)
print(result_indices)
'''
'''
str1 = "catcatfoxfox"
words = ["cat", "fox"]

word_frequency = {}
matched_word = 0
result_indices = []
window_start = 0

for i in words:
    if i not in word_frequency:
        word_frequency[i] = 0
    word_frequency[i] += 1

for window_end in range(0, len(str), len(words[0])):
    str_word = str1[window_end:window_end + len(words[0])]
    if str_word in word_frequency:
        word_frequency[str_word] -= 1
    if word_frequency[str_word] == 0:
        matched_word += 1
    if matched_word == len(words):
        left_char =
        result_indices.append(window_end-len(words[0]))
    print(word_frequency)
print(result_indices)
'''

'''
#Sliding Window Problem Challenge 3
str = "abdbca"
pattern = "abc"
dict1 = {}
window_start = 0
matched = 0
min_length = len(str) + 1

for i in range(len(pattern)):
    if pattern[i] not in dict1:
        dict1[pattern[i]] = 0
    dict1[pattern[i]] += 1

for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in dict1:
        dict1[right_char] -= 1
        if dict1[right_char] == 0:
            matched += 1

    while matched == len(pattern):

        if min_length > window_end - window_start + 1:
            min_length = window_end - window_start + 1
            window_start_tracker = window_start

        left_char = str[window_start]
        if left_char in dict1:
            if dict1[left_char] == 0:
                matched -= 1

            dict1[left_char] += 1
        window_start += 1

if min_length > len(str):
    print("")
print(str[window_start_tracker:window_start_tracker+min_length])
'''
'''
#Sliding window Problem Challenge 2
str = "abbcabc"
pattern = "abc"
dict1 = {}
window_start = 0
matched_letter = 0
arr = []

for i in range(len(pattern)):
    if pattern[i] not in dict1:
        dict1[pattern[i]] = 0
    dict1[pattern[i]] += 1

for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in dict1:
        dict1[right_char] -= 1
        if dict1[right_char] == 0:
            matched_letter += 1
    if window_end - window_start + 1 > len(pattern):
        left_char = str[window_start]
        if left_char in dict1:
            if dict1[left_char] == 0:
                matched_letter -= 1
            dict1[left_char] += 1
        window_start += 1

    if matched_letter == len(dict1):
        for i in range(window_start, window_end + 1):
            arr.append(i)
        print(arr)
print("yo")
'''
'''
#Sliding Window Problem Challenge 1
str = "aaacb"
pattern = "abc"
dict1 = {}
window_start = 0
matched_letter = 0
for i in range(len(pattern)):
    if pattern[i] not in dict1:
        dict1[pattern[i]] = 0
    dict1[pattern[i]] += 1

for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char in dict1:
        dict1[right_char] -= 1
        if dict1[right_char] == 0:
            matched_letter += 1

    if window_end - window_start + 1 > len(pattern):
        left_char = str[window_start]
        if left_char in dict1:
            if dict1[left_char] == 0:
                matched_letter -= 1
            dict1[left_char] += 1
        window_start += 1
    if matched_letter == len(dict1):
        print(True)

print(False)
'''

'''
str = "aaaacb"
pattern = "abc"
dict1 = {}
counter = 0
maximum_count = 0
window_end = len(pattern)
window_start = 0

for i in range(len(pattern)):
    if pattern[i] not in dict1:
        dict1[pattern[i]] = 0
    dict1[pattern[i]] += 1

for i in range(window_start, window_end):
    if str[i] in dict1:
        dict1[str[i]] -= 1
    if dict1[str[i]] < 0:
        
'''



'''
#Longest subarray with Ones after Replacement (hard)
Array = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k = 3
maxOnesCount = 0
window_start = 0
max_length = 0
for window_end in range(len(Array)):
    if (Array[window_end]) == 1:
        maxOnesCount += 1
    elif (Array[window_end]) == 0:
        while window_end - window_start + 1 - maxOnesCount > k:
            if Array[window_start] == 1:
                maxOnesCount -= 1
            window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

print(max_length)
'''

'''
#Long substring with same letters after replacement 
str = "aabccbb"
k = 2
dict1 = {}
window_start = 0
max_length = 0
max_count = 0

for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in dict1:
        dict1[right_char] = 0
    dict1[right_char] += 1

    max_count = max(max_count, dict1[right_char])
    if (window_end - window_start + 1 - max_count) > k:
        left_char = str[window_start]
        dict1[left_char] -= 1
        window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

print(max_length)
'''

'''
#No-repeat Substring
str = "abbbb"
window_start = 0
char_index_map = {}
maximum = float('-inf')
max_length = 0

for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in char_index_map:
        char_index_map[right_char] = 0
    char_index_map[right_char] += 1

    if 2 in char_index_map.values():
        maximum = max(maximum, window_end - window_start)
        window_start = window_end
        char_index_map.clear()
print(maximum)
'''
//
'''
#Longest subarray with Ones after Replacement (hard)
Array = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
k = 3
maxOnesCount = 0
window_start = 0
max_length = 0
for window_end in range(len(Array)):
    if (Array[window_end]) == 1:
        maxOnesCount += 1
    elif (Array[window_end]) == 0:
        while window_end - window_start + 1 - maxOnesCount > k:
            if Array[window_start] == 1:
                maxOnesCount -= 1
            window_start += 1

    max_length = max(max_length, window_end - window_start + 1)
//
print(max_length)
'''

'''
#Long substring with same letters after replacement 
str = "aabccbb"
k = 2
dict1 = {}
window_start = 0
max_length = 0
max_count = 0

for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in dict1:
        dict1[right_char] = 0
    dict1[right_char] += 1

    max_count = max(max_count, dict1[right_char])
    if (window_end - window_start + 1 - max_count) > k:
        left_char = str[window_start]
        dict1[left_char] -= 1
        window_start += 1

    max_length = max(max_length, window_end - window_start + 1)
//
print(max_length) 
'''


'''
#No-repeat Substring
str = "abbbb"
window_start = 0
char_index_map = {}
maximum = float('-inf')
max_length = 0

for window_end in range(len(str)):
    right_char = str[window_end]
    if right_char not in char_index_map:
        char_index_map[right_char] = 0
    char_index_map[right_char] += 1

    if 2 in char_index_map.values():
        maximum = max(maximum, window_end - window_start)
        window_start = window_end
        char_index_map.clear()
print(maximum)
'''
'''
str = "abccde"
window_start = 0
char_index_map = {}
maximum = float('-inf')
max_length = 0

for window_end in range(len(str)):
    print("we are at:",window_end)
    right_char = str[window_end]
    if right_char in char_index_map:
        window_start = max(window_start, char_index_map[right_char] + 1)
        print("start:",window_start)
    char_index_map[right_char] = window_end
    print(char_index_map)
    print("end:", window_end)

    max_length = max(max_length, window_end - window_start + 1)
    print("max_length:",max_length)
print("max:",max_length)
'''
'''
#fruits into basket
fruits = ['A', 'B', 'C', 'A', 'C']
window_start = 0
fruit_frequency = {}
maximum = float('-inf')

for window_end in range(len(fruits)):
    if fruits[window_end] not in fruit_frequency:
        fruit_frequency[fruits[window_end]] = 0
    fruit_frequency[fruits[window_end]] += 1

    while len(fruit_frequency) > 2:
        fruit_frequency[fruits[window_start]] -= 1
        if fruit_frequency[fruits[window_start]] == 0:
            del fruit_frequency[fruits[window_start]]
        window_start += 1
    maximum = max(maximum, window_end - window_start + 1)
print(maximum)
'''
'''
#Longest Substring
str = "araaci"
k = 1

window_start = 0
max_length = 0
char_frequency = {}
maximum = float('-inf')

for window_end in range(len(str)):
    if str[window_end] not in char_frequency:
        char_frequency[str[window_end]] = 0
    char_frequency[str[window_end]] += 1

    while len(char_frequency) > k:
        char_frequency[str[window_start]] -= 1
        if char_frequency[str[window_start]] == 0:
            del char_frequency[str[window_start]]
        window_start += 1
    maximum = max(maximum, window_end - window_start + 1)
print(maximum)
'''


'''
import math
arr = [2, 1, 5, 2, 3, 2]
s = 7
window_sum = 0
min_length = math.inf
window_start = 0

for window_end in range(0, len(arr)):
    window_sum += arr[window_end]
    while window_sum >= s:
        min_length = min(min_length, window_end - window_start + 1)
        print("end:",window_end)
        print("start:",window_start)
        window_sum -= arr[window_start]
        window_start += 1
if min_length == math.inf:
    print(0)
print(min_length)
'''
'''
# window sliding smallest subarray with a given sum 
windowSum = 0.0
windowStart = 0
minimum = float('inf')
arr = [2, 1, 5, 2, 3, 2]
s = 7
for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]
    if windowSum >= s:
        minimum = min(minimum, (windowEnd - windowStart)+1)

        windowSum -= arr[windowStart]
        while windowSum >= s:
            windowStart += 1
            windowSum -= arr[windowStart]
            minimum = min(minimum, (windowEnd - windowStart)+1)
            print("end:", windowEnd)
            print("start:", windowStart)
        windowStart += 1
print(minimum)
'''


'''
nums = [1,2,3,4]
n = len(nums)
leftProduct = [1] * n
rightProduct = [1] * n
# [1, 1, 1, 1]

# build left multipler
for i in range(1, len(nums)):
    leftProduct[i] = leftProduct[i - 1] * nums[i - 1]

# build right multipler
for i in reversed(range(0, len(nums) - 1)):
    # print(rightProduct)
    rightProduct[i] = rightProduct[i + 1] * nums[i + 1]

# combine final list
for i in range(len(nums)):
    nums[i] = leftProduct[i] * rightProduct[i]

print(nums)

# [0, 1, 0, 2, 4]
'''
'''
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5

result = []
windowSum, windowStart = 0.0, 0
for windowEnd in range(len(arr)):
    windowSum += arr[windowEnd]
    #slide the window
    if windowEnd >= K - 1:
        result.append(windowSum / K)
        windowSum -= arr[windowStart]
        windowStart += 1
print(result)

maximum = float('-inf')
maximum = max(maximum, 2)
print(maximum)
'''



'''
result = []
for i in range(len(arr) - K + 1):
    _sum = 0.0
    for j in range(i, i+K):
        _sum += arr[j]
    result.append(_sum/K)
print(result)
'''

'''
prices = [7,1,5,3,6,4]

maximum = 0
minimum = float('inf')
#minimum = 1
for i in range(len(prices)):
    if prices[i] < minimum:
        minimum = prices[i]

    else:
        maximum = max(maximum, prices[i]-minimum)
print(maximum)
'''
'''
dicti = {}
nums = [1,2,3,1,1]
for i in (nums):
    if i not in dicti:
        dicti[i] = 0
    dicti[i]+=1
print(dicti)
for j in dicti:
    print(dicti[j])
'''
'''
nums = [1,2,3,4]

n = len(nums)
forward = [0] * n #[0,0,0,0]
backward = [0] * n #[0,0,0,0]
forward[0] = 1 #[1,0,0,0]
backward[-1] = 1 #[0,0,0,1]
out = [0]*n #[0,0,0,0]

for i in range(n-1):
    forward[i+1] = forward[i] * nums[i]
#forward[1] = forward[0] * nums[0]
print(forward)

for i in range(n-1,0,-1):
    backward[i-1] = backward[i] * nums[i]
print(backward)
for i in range(n):
    out[i] = forward[i] * backward[i]
print(out)
'''


'''
nums = [1,2,3,4]

newnum = 1
newList = []
anotherList = []
tracker = nums[0]
result = 1
for i in range(len(nums)):
    newList.append(nums[i+1:]+nums[:i])

for i in newList:
    for j in i:
        result = result * j
    anotherList.append(result)
    result = 1

print(anotherList)
'''
