"""
Given a string, find the length of the longest substring without repeating
characters.

Found in:
    https://leetcode.com/problems/longest-substring-without-repeating-characters/

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""


def longest_substring(string):
    """
    time: O(n)
    """
    last_seen = {}
    start = 0  # for single char inputs
    max_length = 0

    for i, char in enumerate(string):
        if char in last_seen and last_seen[char] + 1 > start:
            start = last_seen[char] + 1
        last_seen[char] = i
        if i - start + 1 > max_length:
            max_length = i - start + 1
    return max_length
