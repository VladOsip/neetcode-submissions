class Solution:
    def string_to_ascii(self, text: str) -> list[int]:
        return [ord(char) for char in text]

    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        digits1 = [val - 48 for val in self.string_to_ascii(num1)]
        digits2 = [val - 48 for val in self.string_to_ascii(num2)]

        res = [0] * (len(digits1) + len(digits2))

        for i in range(len(digits1) - 1, -1, -1):
            for j in range(len(digits2) - 1, -1, -1):
                mul = digits1[i] * digits2[j]
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]

                res[p2] = total % 10
                res[p1] += total // 10

        start_index = 1 if res[0] == 0 else 0
        return "".join(chr(digit + 48) for digit in res[start_index:])
