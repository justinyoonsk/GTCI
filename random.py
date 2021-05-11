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
