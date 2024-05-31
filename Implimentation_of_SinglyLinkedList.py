class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position): # Enables the user to insert a data at an place 
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range") # Informs the user to locate the data correctly
            current = current.next
        if current is None:
            raise IndexError("Position out of range")
        new_node.next = current.next
        current.next = new_node

    def delete_at_position(self, position): # Enables the user to delete unwanted or redundant data if any 
        if self.head is None:
            raise IndexError("Position out of range")
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 1):
            if current is None or current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        current.next = current.next.next

    def delete_after_node(self, prev_node):
        if prev_node is None or prev_node.next is None:
            raise ValueError("Previous node is not in the list or has no next node")
        prev_node.next = prev_node.next.next

    def search_node(self, key): # Enables the user to look for the data what he/she want 
        current = self.head
        position = 0
        while current is not None:
            if current.data == key:
                return position
            current = current.next
            position += 1
        return -1

    def print_list(self): # Displays available list of data
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

# Stack implementation using linked list
class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self): # Checks whether the Stack is empty or not ?
        return self.head is None

    def push(self, data): # Adds a data a the end the stack
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):# Deletes a data that appear at the end of the stack
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def peek(self):# Picks the last element of the stack and the displays that element only 
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.head.data

    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

# Example usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_position(10, 0)
    sll.insert_at_position(20, 1)
    sll.insert_at_position(30, 2)
    sll.print_list()

    sll.delete_at_position(1)
    sll.print_list()

    sll.delete_after_node(sll.head)
    sll.print_list()

    print(sll.search_node(10))
    print(sll.search_node(20))

    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()

    print(stack.pop())
    print(stack.peek())
    stack.print_stack()
