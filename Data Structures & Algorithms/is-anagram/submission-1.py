class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        seenS = defaultdict(int)
        for ch in s:
            seenS[ch] += 1
        
        seenT = defaultdict(int)
        for ch in t:
            seenT[ch] += 1
        
        if seenS == seenT:
            return True

        return False

