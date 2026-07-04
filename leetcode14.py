class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""
        index = 0
        
        while len(prefix) < len(strs[0]):
            new_prefix = prefix + strs[0][index]
            for string in strs:
                if not string.startswith(new_prefix):
                    return prefix
            prefix = new_prefix
            index+=1

        return prefix