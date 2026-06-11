class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        end = len(s1)
        need = defaultdict(int)
        window = defaultdict(int)

        for c in s1:
            need[c] += 1

        start = 0
        
        for end in range(len(s2)):
            window[s2[end]] += 1

            if end - start + 1 > len(s1):
                window[s2[start]] -= 1
                if window[s2[start]] == 0:
                    del window[s2[start]]
                start+=1

            if window == need:
                return True
        
        return False
            

        
        