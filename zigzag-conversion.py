class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s

        parts = ["" for _ in range(numRows)]
        step = -1
        row = 0

        for i, c in enumerate(s):
            parts[row] += c
            if row == 0 or row == numRows - 1:
                step = -step

            row += step

        return "".join(parts)


if __name__ == '__main__':
    solution = Solution()
    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert solution.convert("A", 1) == "A"
    assert solution.convert("ABC", 2) == "ACB"
