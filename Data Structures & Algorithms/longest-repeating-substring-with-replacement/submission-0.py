class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        longest = 0
        seen = {}

        for end in range(len(s)):
            if s[end] not in seen:
                seen[s[end]] = 0
            seen[s[end]] += 1
            maxFreq = max(seen.values())
            windowsize = end - start + 1

            while windowsize - maxFreq > k:
                seen[s[start]] -=1 
                start+=1
                maxFreq = max(seen.values())
                windowsize = end - start + 1

            replacement = windowsize - maxFreq

            if replacement <= k:
                longest = max(longest, windowsize)

        return longest









