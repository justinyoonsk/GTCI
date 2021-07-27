'''
input: [1, 3, 3, 5]
output: [], [1], [3], [1, 3], [3, 3], [1, 3, 3], [5],
[1, 5], [3, 5], [1, 3, 5], [3, 3, 5], [1, 3, 3, 5]
                                   []
                            copy  / \ add 1
                                [] | [1]
                        copy    /       \ add 3
                            [] [1] | [3] [1, 3]
                        copy     /       \ add 3
                    [] [1] [3] [1, 3] | [3, 3] [1, 3, 3]
               copy  /                                 \ add 5
[] [1] [3] [1, 3] [3, 3] [1, 3, 3] | [5] [1, 5] [3, 5] [1, 3, 5] [3, 3, 5] [1, 3, 3, 5]

'''


def find_subsets(nums):
    list.sort(nums)
    subsets = []
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets) - 1
        for j in range(startIndex, endIndex + 1):
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

#  time complexity: O(N *2^N)
# space complexity: O(N *2^N)

