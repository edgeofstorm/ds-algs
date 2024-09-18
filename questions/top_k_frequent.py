"""
Top K Elements in List
Solved 
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

"""

from typing import List


def solution(nums: List[int], k: int) -> List[int]:
    """Given an integer array nums and an integer k, return the k most frequent elements within the array."""
    occurance = {}

    for num in nums:
        if num in occurance:
            occurance[num] += 1
            continue
        occurance[num] = 1

    return sorted(occurance, key=lambda num: occurance[num], reverse=True)[:k]


if __name__ == "__main__":
    assert solution([1, 2, 2, 3, 3, 3], 2) == [3, 2]
    assert solution(nums=[7, 7], k=1) == [7]
    assert solution([1, 2, 2, 3, 3, 3], 3) == [3, 2, 1]
