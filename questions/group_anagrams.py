"""
Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""

from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if len(strs) < 2:
        return [strs]

    sorted_strs = {}
    for string in strs:
        if "".join(sorted(string)) in sorted_strs:
            sorted_strs["".join(sorted(string))].append(string)
            continue
        sorted_strs["".join(sorted(string))] = [string]

    return sorted_strs.values()


if __name__ == "__main__":
    assert groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]) == [
        ["act", "cat"],
        [
            "pots",
            "tops",
            "stop",
        ],
        ["hat"],
    ]
    assert groupAnagrams(["x"]) == [["x"]]
