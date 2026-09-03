class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        parentheses = []

        def backtrack(currentString, openBracket, closedBracket):

            if openBracket != n:
                backtrack(currentString + "(", openBracket + 1, closedBracket)

            if openBracket > closedBracket:
                backtrack(currentString + ")", openBracket, closedBracket + 1)

            if len(currentString) == 2 * n:
                parentheses.append(currentString)
                return
        
        backtrack("", 0, 0)
        return parentheses
        