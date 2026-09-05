class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # dp for one single character is a palindrome 
        # s[i] == s[j] then its true, continue?
        # add it? 
        results = []
        current = []

        def isPalindrome(word):
            return word == word[::-1]

        def backtrack(start):
            if start == len(s):
                results.append(current.copy())
                return
                
            for end in range(start, len(s)):

                substring = s[start:end+1]

                if not isPalindrome(substring):
                    continue

                else:
                    current.append(substring)
                    backtrack(end + 1)
                    current.pop()

        backtrack(0)
        return results
                