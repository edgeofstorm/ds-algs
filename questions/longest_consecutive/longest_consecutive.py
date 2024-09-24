"""
Longest Consecutive Sequence
Given an array of integers nums, return the length of the longest consecutive sequence of elements.

A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [2,20,4,10,3,4,5]

Output: 4
Explanation: The longest consecutive sequence is [2, 3, 4, 5].

Example 2:

Input: nums = [0,3,2,5,4,6,1,1]

Output: 7
Constraints:

0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    # # O(n2)
    # longest = 0
    # seen = set()
    # for num in nums:
    #     if num in seen:
    #         continue
    #     inner_longest = 0
    #     consecutive_start = num
    #     while consecutive_start + 1 in nums:
    #         seen.add(consecutive_start + 1)
    #         consecutive_start += 1
    #         inner_longest += 1
    #     longest = max(inner_longest, longest)
    # return longest + 1

    # # O(nlogn)
    # if not nums:
    #     return 0

    # max_longest = 0
    # longest = 0
    # sorted_nums = sorted(list(set(nums)))  # use sorted sets maybe
    # for index in range(len(sorted_nums) - 1):
    #     if sorted_nums[index] + 1 == sorted_nums[index + 1]:
    #         longest += 1
    #         max_longest = max(max_longest, longest)
    #     else:
    #         longest = 0
    # return max_longest + 1

    # O(n)
    # convert the input list to set - to perform left neighbour checks
    # loop through list to determine sequence starters (if the element does not have a left neighbour its a sequence starter)
    # Though the solution may look like quadratic due to the while loop inside the for loop,
    # the while loop only gets executed at the start of a sequence when (n-1) is not found in the set.
    # Worst case for a sorted array, the first pass will run the while loop (n-1) times, but all other run it will not get executed at all.
    # so the while loop will only run a total of n times for the entire length of the solution.
    # so the complexity is O(n+n) which is O(n)..
    longest = 0
    nums_set = set(nums)
    for num in nums_set:
        if num - 1 in nums_set:
            continue
        length = 0
        while num + length in nums_set:
            length += 1
        longest = max(longest, length)
    return longest


if __name__ == "__main__":
    assert longestConsecutive(nums=[2, 20, 21, 22, 23, 24, 25, 10, 3, 4, 5]) == 6
    assert longestConsecutive(nums=[2, 20, 4, 10, 3, 4, 5]) == 4
    assert longestConsecutive(nums=[0, 3, 2, 5, 4, 6, 1, 1]) == 7
