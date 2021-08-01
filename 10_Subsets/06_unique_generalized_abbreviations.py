'''
input: "BAT"
output: "BAT", "BA1", "B1T", "B2", "1At", "1A1", "2T", "3"

input: "code"
output: "code", "cod1", "co1e", "co2", "c1de", "c1d1', "c2e", c3", "1ode", "1od1", "1o1e", "1o2",
"2de", "2d1", "3e", "4"

add B:         _ B
add A:      __ 1A B_ BA
add T: ___ 2T 1A_ 1AT B__ B1T BA_ BAT
    3   2T   1A1   1AT   B2   B1T   BA1   BAT

'''

from collections import deque


class AbbreviateWord:

    def __init__(self, s, start, count):
        self.s = s
        self.start = start
        self.count = count

def generate_generalized_abbreviation(word):
    wordLen = len(word) #3
    result = []
    queue = deque()
    queue.append(AbbreviateWord(list(), 0, 0))

    while queue:
        abWord = queue.popleft() #[],0,0 #[],1,1 #[B],1,0
        if abWord.start == wordLen:
            if abWord.count != 0:
                abWord.s.append(str(abWord.count))
            result.append("".join(abWord.s))
        else:
            queue.append(AbbreviateWord(list(abWord.s),abWord.start+1, abWord.count+1))
            #[],1,1
            #[],2,2
            #[B],2,1

            if abWord.count != 0:
                abWord.s.append(str(abWord.count))
                #[1],1,1

            newWord = list(abWord.s) #[] #[1] #[B]
            newWord.append(word[abWord.start]) #[1B] #[B
            print(newWord)
            queue.append(AbbreviateWord(newWord, abWord.start+1, 0))
            #[B],1,0
            #[1A],2,0

    return result

def main():
    print("Generalized abbreviation are: " + str(generate_generalized_abbreviation(("BAT"))))

main()

#time complexity: O(N*2^N)
#space complexity O(N*2^N)
