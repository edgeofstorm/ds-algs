"""
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

"""


def solution(s: str, t: str) -> bool:
    # pythonic
    # from collections import Counter
    # return Counter(s) == Counter(t)

    # O(1) memory
    return sorted(s) == sorted(t)

    # sol 1
    if len(s) != len(t):
        return False

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1

    return all([x == 0 for x in char_count.values()])

    # sol 2
    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    for char in count_s:
        if count_s[char] != count_t.get(char):
            return False

    return True


if __name__ == "__main__":
    assert solution(s="racecar", t="carrace") == True
    assert solution(s="jar", t="jam") == False
    assert solution(s="ccbc", t="bbcc") == False
