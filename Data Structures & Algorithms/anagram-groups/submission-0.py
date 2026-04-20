class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map=defaultdict(list)
        for i in strs:
            sorted_words=''.join(sorted(i))
            hash_map[sorted_words].append(i)
        return list(hash_map.values())    