class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        compareWord = strs[0]
        ans = []

        for i, s in enumerate(compareWord):
            for word in strs:
                if i >= len(word) or s != word[i]:
                    return "".join(ans)
            ans.append(s)
        
        return "".join(ans)
                    




        