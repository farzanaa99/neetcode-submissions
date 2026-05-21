class Solution:
    def isPalindrome(self, s: str) -> bool:

        start = 0
        end = len(s)-1

        punctuation = "?.;:, '"

        while start <= end:

            if s[start] in punctuation:
                start+=1
                continue

            elif s[end] in punctuation:
                end-=1
                continue

            if s[start].lower() != s[end].lower():
                return False

            start+=1
            end-=1
        
        return True
        