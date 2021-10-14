# 819. 가장 흔한 단어
'''
금지된 단어를 제외한 가장 빈도수가 높은 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 또한 무시한다.
'''

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