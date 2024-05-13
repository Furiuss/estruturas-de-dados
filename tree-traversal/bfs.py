class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.length = 0    
        
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True            
            if temp.value > value:
                temp = temp.left
            else:
                temp = temp.right
        return False
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)
                
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left != None:                
                queue.append(current_node.left)
            if current_node.right != None:
                queue.append(current_node.right)
        return results
    
arvore = BinarySearchTree()
arvore.insert(47)
arvore.insert(21)
arvore.insert(76)
arvore.insert(18)
arvore.insert(27)
arvore.insert(52)
arvore.insert(82)

print(arvore.BFS())