class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        result = []
        
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, current_combination):
            if len(current_combination) == len(digits):
                result.append("".join(current_combination))
                return
            
            current_digit = digits[index]
            possible_letters = phone[current_digit]
            
            for letter in possible_letters:
                current_combination.append(letter)                
                backtrack(index + 1, current_combination)
                current_combination.pop()

        backtrack(0, [])
        return result