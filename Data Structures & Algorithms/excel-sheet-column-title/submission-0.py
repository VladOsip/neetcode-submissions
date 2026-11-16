class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result.append(chr(ord('A') + remainder))
            
        return "".join(reversed(result))