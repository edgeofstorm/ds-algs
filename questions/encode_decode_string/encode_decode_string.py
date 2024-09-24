"""
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.


"""

from typing import List


def encode(strs: List[str]) -> str:
    res = ""
    for s in strs:
        res += f"{len(s)}#{s}"
    return res


def decode(s: str) -> List[str]:
    res, i = [], 0

    while i < len(s):
        j = i
        while s[j] != "#":
            j += 1
        length = int(s[i:j])
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length

    return res

    # for index, char in enumerate(s):
    #     if char == "#" and s[index - 1].isnumeric():
    #         k = index - 1
    #         digit = s[index - 1]
    #         while digit.isdigit():
    #             digit = s[k - 1 : index - 1]
    #             k -= 1
    #         strs.append(s[index + 1 : index + 1 + int(s[index - 1])])
    # return strs


if __name__ == "__main__":
    assert decode(encode(["neet", "code", "love", "you"])) == [
        "neet",
        "code",
        "love",
        "you",
    ]
    assert decode(encode(["we", "say", ":", "yes"])) == ["we", "say", ":", "yes"]
