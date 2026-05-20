class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        table = {}

        for s in strs:

            sortedstring = "".join(sorted(s))
            if sortedstring not in table:
                table[sortedstring] = []
            table[sortedstring].append(s)
  
        return list(table.values())
            

