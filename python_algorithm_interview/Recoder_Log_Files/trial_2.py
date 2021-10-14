# 937. 로그파일 재정렬
'''
다음 기준으로 정렬합니다.
1. 로그의 가장 앞부분은 식별자다
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다
4. 숫자 로그는 입력 순서대로 한다
'''

logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]


class Solution:
    def reorderLogFiles(self, logs):
        char_list = []
        num_list = []

        for log in logs:
            if log[-1].isalpha():
                char_list.append(log)
                char_list.sort(key=lambda x: (x.split()[1:], x.split()[0]))
            else:
                num_list.append(log)

        return char_list + num_list


test = Solution()
print(test.reorderLogFiles(logs))