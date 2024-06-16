# https://leetcode.com/problems/longest-repeating-character-replacement/

def characterReplacement(self, s: str, k: int) -> int:
    count = {}  #hashmap to store count of each character in current substring
    res = 0
    l = 0

    for r in range(len(s)):
        #increment count for right character, if character doesn't exist in hashmap, use default 0
        count[s[r]] = 1 + count.get(s[r], 0)    

        # while size of window minus count of most popular character is greater than allowed replacement, 
        # decrement count of left character count and increment left pointer (shrink window)
        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1

        res = max(res, r - l + 1)
    return res
