# 49. 그룹 애너그램
# https://leetcode.com/problems/group-anagrams/
'''
문자열 배열을 받아 애너그램 단위로 그룹핑하라
'''

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        dic = defaultdict(list)
        answer = []
        for s in strs:
            s_list = list(s)
            tmp_s = "".join(sorted(s_list))
            dic[tmp_s].append(s)

        for group in dic.values():
            answer.append(group)

        return answer


problem_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
test = Solution()
test.groupAnagrams(problem_list)
