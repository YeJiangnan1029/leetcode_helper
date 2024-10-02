from collections import defaultdict
from typing import List

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # class trie_node:
        #     def __init__(self) -> None:
        #         self.edge = dict()
        #         self.is_end = False

        # trie = trie_node()
        # first_freq = defaultdict(int)
        # n_words = len(ideas)
        # for idea in ideas:
        #     cur_node = trie
        #     for i in range(len(idea)):
        #         t = idea[len(idea)-i-1]
        #         if t not in cur_node.edge:
        #             cur_node.edge[t] = trie_node()
        #         cur_node = cur_node.edge[t]
        #         if i == len(idea)-1:
        #             cur_node.is_end = True
        #             first_freq[t] +=  1
        # self.ret_ans = 0
        # def getans(trie):
        #     cur_son = []
        #     acc_fre = 0
        #     for e in trie.edge:
        #         getans(trie.edge[e])
        #         if trie.edge[e].is_end:
        #             cur_son.append(e)
        #             acc_fre += first_freq[e]
        #     if len(cur_son) > 1:
        #         self.ret_ans += len(cur_son) * (n_words-acc_fre)
        #     elif len(cur_son) == 1:
        #         self.ret_ans += n_words-acc_fre
        # getans(trie)
        # return self.ret_ans

        # 哈希方法
        ret = 0
        suffix_freq = defaultdict(set)
        first_freq = defaultdict(int)
        for idea in ideas:
            first = idea[:1]
            suffix = idea[1:] 
            suffix_freq[first].add(suffix)

        keys = list(suffix_freq.keys())
        for k1 in range(len(keys)):
            for k2 in range(k1+1, len(suffix_freq.keys())):
                set1 = suffix_freq[keys[k1]]
                set2 = suffix_freq[keys[k2]]
                n_1 = len(set1 - set2)
                n_2 = len(set2 - set1)
                ret += n_1 * n_2
        return ret*2

ideas = ["aaa","baa","caa","bbb","cbb","dbb"]
solution = Solution()
print(solution.distinctNames(ideas))