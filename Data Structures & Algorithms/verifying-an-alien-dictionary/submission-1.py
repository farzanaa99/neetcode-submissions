class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        for i in range(len(words) - 1):
            first = words[i]
            second = words[i+1]

            for j in range(len(first)):
                if j >= len(second):
                    return False
                
                if first[j] == second[j]:
                    continue

                if order.index(first[j]) < order.index(second[j]):
                    break
                else:
                    return False

        return True


        