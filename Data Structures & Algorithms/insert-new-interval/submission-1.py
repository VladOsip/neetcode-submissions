from typing import List


class Solution:

    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        points = []
        for s, e in intervals:
            points.append((s, -1))
            points.append((e, 1))

        points.append((newInterval[0], -1))
        points.append((newInterval[1], 1))

        points.sort(key=lambda x: (x[0], x[1]))

        result = []
        checker = 0
        start = None

        for coord, role in points:
            if checker == 0:
                start = coord

            checker += role

            if checker == 0:
                result.append([start, coord])

        return result