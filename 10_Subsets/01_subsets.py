'''
input: [1, 3]
output: [], [1], [3], [1, 3]

input: [1, 5, 3]
output: [], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]

                 []
   copy  /             \ add 1
        []              [1]
copy  /    \          /        \ add 5
    []    [1]       [5]       [1,5]
  /  \  /   \      /  \      /    \
[] [1] [5] [1,5] [3] [1,3] [5,3] [1,5,3]
copy                                add 3
'''

def find_subsets(nums):
    subsets = []
    subsets.append([])
    for currentNumber in nums:
        n = len(subsets)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(currentNumber)
            subsets.append(set1)

    return subsets

def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()

#time complexity: O(N * 2^N)
#space complexity: O(N* 2^N)
