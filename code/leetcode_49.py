from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = {}
        ret_list = []
        for word in strs:
            ordered_word = "".join(sorted(word))
            if ordered_word not in word_dict:
                word_dict[ordered_word] = [word]
            else:
                word_dict[ordered_word].append(word)
        for key in word_dict:
            ret_list.append(word_dict[key])
        return ret_list

s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(s.groupAnagrams(strs))