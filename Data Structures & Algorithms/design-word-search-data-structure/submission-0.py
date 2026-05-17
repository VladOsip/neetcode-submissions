class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def dfs(index, node) -> bool:
            current = node
            
            for i in range(index, len(word)):
                char = word[i]
                
                if char == '.':
                    # If it's a wildcard, check all existing child nodes recursively
                    for child in current.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    # Normal character matching
                    if char not in current.children:
                        return False
                    current = current.children[char]
                    
            return current.is_end_of_word

        return dfs(0, self.root)