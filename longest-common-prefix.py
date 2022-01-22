from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word, max_word = min(strs), max(strs)
        index = 0

        while index < len(min_word) and max_word.startswith(min_word[:index + 1]):
            index += 1

        return min_word[:index]


if __name__ == '__main__':
    solution = Solution()
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["flow", "flow", "flow"]) == "flow"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
