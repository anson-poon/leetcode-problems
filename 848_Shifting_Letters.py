# https://leetcode.com/problems/shifting-letters/description/

'''
You are given a string s of lowercase English letters and an integer array shifts of the same length.
Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
Return the final string after all such shifts to s are applied.


Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"
'''
from itertools import accumulate

def shifting_letters(s, shifts) -> str:
    # Example: abc, [3,5,9]
    # a shift 17 times -> r     Shift: 3 + 5 + 9
    # b shift 14 times -> p     Shift: 5 + 9
    # c shift 9  times -> l     Shift: 9

    # Time Complexity:  O(n)
    # Space Complexity: O(n)

    new_s = ""

    # Get total shifts for each places by accumulating the reversed list, and reverse back to original order
    total_shifts = list(accumulate(shifts[::-1]))[::-1]

    # Shift the letters
    for i, char in enumerate(s):
        # mod 26 to simplify shifts over 26 (e.g. shift 30 == shift 4)
        ascii_index = ord(char) + total_shifts[i] % 26
        if ascii_index > 122:                           # if shift out of bound, wrap around
            ascii_index = ascii_index - 26

        new_s += chr(ascii_index)

    return new_s


print(shifting_letters("abc", [3, 5, 9]))  # rpl
