class CountSquares:

    def __init__(self):
        self.points = Counter() 

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1
        

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0
        for (px, py) in self.points:
            if abs(px - qx) == abs(py - qy) and px != qx:  # 유효한 대각선
                res += (
                    self.points[(px, py)]
                    * self.points[(qx, py)]
                    * self.points[(px, qy)]
                )
        return res
        
