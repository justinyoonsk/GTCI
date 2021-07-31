'''
Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()

can't have more than three open parentheses



    ((())

((()))  (()())   (())()   ()(())   ()()()
'''
from collections import deque

class ParenthesesString:
    def __init__(self, str, openCount, closeCount):
        self.str = str
        self.openCount = openCount
        self.closeCount = closeCount

def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))
    while queue:
        ps = queue.popleft()
        if ps.openCount == num and ps.closeCount == num:
            result.append(ps.str)
        else:
            if ps.openCount < num:
                queue.append(ParenthesesString(ps.str + "(", ps.openCount + 1, ps.closeCount))
            if ps.openCount > ps.closeCount:
                queue.append(ParenthesesString(ps.str + ")", ps.openCount, ps.closeCount + 1))

    return result


def main():
    print("All combinations of balanced parantheses are: " + str(generate_valid_parentheses((3))))

main()

#time complexity: O(4^n/sqrt(n))
#space complexity: O(N*2^N)
