"""
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

from typing import List


def solution(nums: List[int]) -> bool:
    """Given an integer array nums, return true if any value appears more than once in the array, otherwise return false."""
    if not nums:
        return False

    # return not len(set(nums)) == len(nums)

    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    assert solution([1, 2, 3, 4, 5]) == False
    assert solution([1, 2, 2, 4, 5]) == True
    assert solution([]) == False
