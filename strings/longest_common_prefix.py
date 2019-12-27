class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        wordsFrequency = {}
        for word in strs:
            for w in list(set(word)):
                if w in wordsFrequency:
                    wordsFrequency[w] += 1
                else:
                    wordsFrequency[w] = 1
        result = ''
        for k in wordsFrequency.keys():
            if wordsFrequency[k] == len(strs):
                result += k
        return result
