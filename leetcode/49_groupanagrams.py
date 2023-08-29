class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for string in strs:
            tempStr = ''.join(sorted(string))
            dic[tempStr].append(string)
        return (list(dic.values()))