# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict

def groupAnagrams(strs):
    # Time Complexity: O(m*nlogn) where m is the number of strings and n is the length of the longest string
    # Space Complexity: O(m*n)
    
    str_map = defaultdict(list)

    for s in strs:
        sorted_str = ''.join(sorted(s))
        str_map[sorted_str].append(s)
        
    return list(str_map.values())


def groupAnagramsAlternative(strs):
    str_map = {}

    for s in strs:
        sorted_str = ''.join(sorted(s))
        
        if sorted_str not in str_map:
            str_map[sorted_str] = []
        
        str_map[sorted_str].append(s)
        
    return list(str_map.values())