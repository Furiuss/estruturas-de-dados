class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        
    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        
    def prepend(self, value):
        new_node = Node(value)
        temp = self.head
        self.head = new_node
        new_node.next = temp
        
    def pop(self):
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        pre.next = None
        self.tail = pre
    
    def pop_first(self):
        temp = self.head
        self.head = temp.next
        temp = None
        
    def get(self, index):
        temp = self.head
        counter = 0
        while temp:
            if counter == index:
                return temp.value
            counter += 1
            temp = temp.next
        return None
    
    def print_list(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.value))
            temp = temp.next
        values.append("None")
        print(" -> ".join(values))
        
    def reverse(self):
        self.temp = self.tail
        self.tail = self.head
        self.head = temp
        while temp.next:
            
        
        
        
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
print(linked_list.get(1))
# linked_list.print_list()