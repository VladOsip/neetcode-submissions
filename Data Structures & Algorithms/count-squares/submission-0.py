class CountSquares:

    def __init__(self):
        self.point_counts = defaultdict(int)
        self.x_to_y_points = defaultdict(list)

    def add(self, point: list[int]) -> None:
        x, y = point
        self.point_counts[(x, y)] += 1
        self.x_to_y_points[x].append(y)

    def count(self, point: list[int]) -> int:
        px, py = point
        total_squares = 0
        
        # Look at all points that share the same x-coordinate (same vertical line)
        for y in self.x_to_y_points[px]:
            # Skip if it is the query point itself (square must have positive area)
            if y == py:
                continue
                
            # Calculate the side length of the potential square
            side_len = abs(py - y)
            
            # Case 1: The square forms to the right of the query point
            x_right = px + side_len
            total_squares += self.point_counts[(x_right, py)] * self.point_counts[(x_right, y)]
            
            # Case 2: The square forms to the left of the query point
            x_left = px - side_len
            total_squares += self.point_counts[(x_left, py)] * self.point_counts[(x_left, y)]
            
        return total_squares
