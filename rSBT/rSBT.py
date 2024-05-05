class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.length = 0
        
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
            
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def r_delete(self, value):
        self.__r_delete(self.root, value)
    
    def min_value(self, current_node):
        if current_node.left != None:
            current_node = self.min_value(current_node.left)
        return current_node
    
    def __r_insert(self, current_node, value):
        if current_node == None:
           return Node(value)
        if value < current_node.value:
           current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
    
    def __r_delete(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__r_delete(current_node.right, sub_tree_min)
        return current_node
        
arvore = BinarySearchTree()
arvore.r_insert(90)
arvore.r_insert(89)
arvore.r_insert(91)
arvore.r_insert(92)
arvore.r_delete(91)
print(arvore.r_contains(89))
print(arvore.min_value(arvore.root).value)