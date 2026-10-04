func largestRectangleArea(heights []int) int {
	stack := []int{}
	maxArea := 0
	heights = append(heights, 0)

	for i, h := range heights {
		for len(stack) > 0 && heights[stack[len(stack)-1]] >= h {
			heightIndex := stack[len(stack)-1]
			stack = stack[:len(stack)-1]

			height := heights[heightIndex]
			width := i
			if len(stack) > 0 {
				width = i - stack[len(stack)-1] - 1
			}

			if area := height * width; area > maxArea {
				maxArea = area
			}
		}
		stack = append(stack, i)
	}

	return maxArea
}
