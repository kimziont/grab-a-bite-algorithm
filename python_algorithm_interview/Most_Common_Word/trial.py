import re
from collections import Counter

class Solution:

    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        # .;,과 같은 다양한 부호로 단어가 구분될 수 있다 -> 띄어쓰기로 통일
        paragraph = re.sub('[^a-z ]', ' ', paragraph)
        counter = Counter(paragraph.split())

        for ban in banned:
            if ban in counter:
                counter.pop(ban)

        answer = counter.most_common(1)
        print(answer[0][0])


paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

test = Solution()
test.mostCommonWord(paragraph, banned)