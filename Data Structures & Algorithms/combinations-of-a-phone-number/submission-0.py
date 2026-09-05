class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"   
        }

        results = []
        current = ""

        if not digits:
            return results

        def backtrack(current, i):
            if i == len(digits):
                results.append(current)
                return

            for letter in phone[digits[i]]:
                backtrack(current + letter, i + 1)

        backtrack(current, 0)
        return results


        