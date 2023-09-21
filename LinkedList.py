class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, node):
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next_node is not None:
            temp = temp.next_node
        temp.next_node = node

    def search(self,data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next_node
        return False


    def display(self):
        temp = self.head
        while temp is not None:
            print(f"{temp.data}---->",end='')
            temp = temp.next_node
        print("/",end='')

    def update(self,data,updated_data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                temp.data=updated_data
                return
            temp = temp.next_node
        raise ValueError(f"{data} not found in linked list")

    def delete(self,data):
        if self.head.data == data:
            self.head = self.head.next_node
            return
        temp = self.head.next_node
        prev = self.head
        while temp is not None:
            if temp.data == data:
                prev.next_node = temp.next_node
                return
            prev=temp
            temp=temp.next_node
        raise ValueError(f"{data} not found in linked list")
