class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the full word at the leaf node for easy retrieval

    def add_word(self, word: str):
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie
        root = TrieNode()
        for word in words:
            root.add_word(word)
            
        rows, cols = len(board), len(board[0])
        result = []

        # 2. Define the Backtracking DFS function
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # If we matched a full word, add it to our results
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None # Mark as None so we don't duplicate it

            # Mark the current cell as visited using a placeholder
            board[r][c] = '#'

            # Explore all 4 adjacent directions (Up, Down, Left, Right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)

            # Backtrack: Restore the original character
            board[r][c] = char

            # Optimization: Pruning the Trie. 
            # If the current node has no children left, remove it from the parent.
            if not curr_node.children:
                parent_node.children.pop(char)

        # 3. Step through every cell in the board to start the search
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return result