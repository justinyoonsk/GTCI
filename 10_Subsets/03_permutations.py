'''
[]
[1]
[3, 1] [1, 3]
[5, 3, 1] [3, 5, 1] [3, 1, 5] [5, 1, 3] [1, 5, 3] [1, 3, 5]

'''
from collections import deque

def find_permutations(nums):
    result = []
    find_permutations_recursive(nums, 0, [], result)
    return result

def find_permutations_recursive(nums, index, currentPermutation, result):
    if index == len(nums):
        result.append(currentPermutation)
    else:
        for i in range(len(currentPermutation)+1):
            newPermutation = list(currentPermutation)
            newPermutation.insert(i, nums[index])
            find_permutations_recursive(nums, index + 1, newPermutation, result)



def main():
    print("Here are all the permutations " + str(find_permutations([1, 3, 5])))

main()
