class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenS = {}
        for ch in s:
            if ch not in seenS:
                seenS[ch] = 1
            else:
                seenS[ch] += 1
        
        for ch in t:
            if ch not in seenS:
                return False
                
            if ch in seenS:
                seenS[ch] -= 1

            if seenS[ch] <= 0:
                del seenS[ch]

        if len(seenS) == 0:
            return True
        else:
            return False
            
