class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_unique_trees(n):
    if n <= 0:
        return []
    return findUnique_trees_recursive(1, n)

def findUnique_trees_recursive(start, end):
    result = []
    if start > end:
        result.append(None)
        return result

    for i in range(start, end+1):
        leftSubtrees = findUnique_trees_recursive(start, i - 1)
        rightSubtrees = findUnique_trees_recursive(i + 1, end)
        for leftTree in leftSubtrees:
            for rightTree in rightSubtrees:
                root = TreeNode(i)
                root.left = leftTree
                root.right = rightTree
                result.append(root)

    return result


def main():
    print("Total trees: " + str(len(find_unique_trees(3))))


main()

#time complexity O(N*2^N)
#space complexity O(2^N)

