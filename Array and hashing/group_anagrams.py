## Explaination: https://leetcode.com/problems/group-anagrams/
## We can sort the strings and then use the sorted string as a key in the dictionary
## and append the original string to the list of values for that key
## Finally we return the values of the dictionary

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(lambda:[])
        for i in strs:
            c = "".join(sorted(i))
            d[c].append(i)
        return list(d.values())

        