class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        char2idx = dict()

        for i, c in enumerate(s):
            if c in char2idx:
                max_length = max(len(char2idx), max_length)
                char2idx = {s[j]: j for j in range(char2idx[c] + 1, i)}

            char2idx[c] = i

        return max(len(char2idx), max_length)


if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("") == 0
    assert solution.lengthOfLongestSubstring(" ") == 1
    assert solution.lengthOfLongestSubstring("bpfbhmipx") == 7
    assert solution.lengthOfLongestSubstring("umvejcuuk") == 6

