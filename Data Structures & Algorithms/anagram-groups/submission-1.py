class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in seen:
                seen[sortedWord] = []
            seen[sortedWord].append(word)
        ans = []
        for key, value in seen.items():
            ans.append(value)

        return ans

        