'''
input: "ad52"
output: "ad52", "Ad52", "aD52", "AD52"

input: "ab7c"
output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C","

                          ab7c
                        /       \
                    [ab7c]      [Ab7c]
                    /               \
            [ab7c] [Ab7c]       [aB7c] [AB7c]
                /                       \
[ab7c] [Ab7c] [aB7c] [AB7c] | [ab7C] [Ab7C] [aB7C] [AB7c]
'''
def find_letter_case_string_permutation(str):
    permutations = []
    permutations.append(str)
    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append("".join(chs))

    return permutations

def main():
    print("String permutations are: " + str(find_letter_case_string_permutation(("ad52"))))
    print("String permutations are: " + str(find_letter_case_string_permutation("ab7c")))

main()

#time complexity: O(N*2^N)
#space complexity: O(N*2^N)
