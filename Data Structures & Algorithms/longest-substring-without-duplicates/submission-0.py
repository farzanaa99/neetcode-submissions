class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        longest = 0
        seen = set()

        for end in range(len(s)):
            while s[end] in seen:
                seen.remove(s[start])
                start+=1
            seen.add(s[end])
            longest = max(longest, end - start + 1)

        return longest
        