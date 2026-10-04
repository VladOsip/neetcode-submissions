class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        counter1 = [0] * 26
        counter2 = [0] * 26

        for i in range(len(s1)):
            counter1[ord(s1[i]) - ord('a')] += 1
            counter2[ord(s2[i]) - ord('a')] += 1

        if counter1 == counter2:
            return True

        for right in range(len(s1), len(s2)):
            counter2[ord(s2[right]) - ord('a')] += 1
            counter2[ord(s2[right - len(s1)]) - ord('a')] -= 1

            if counter1 == counter2:
                return True

        return False