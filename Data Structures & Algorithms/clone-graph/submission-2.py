class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        clones = {node: Node(node.val)}
        keys = [node]
        
        i = 0
        while i < len(keys):
            current = keys[i]
            for neighbor in current.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    keys.append(neighbor)
                clones[current].neighbors.append(clones[neighbor])
            i += 1
                
        return clones[node]