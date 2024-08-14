class node:
    def __init__(self, data= None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = node()

    def linked_append(self, data):
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
    
    def length(self):
        total = 0
        curr = self.head
        while curr.next != None:
            total += 1
            curr = curr.next
        print(f"Total elements in linked list is: {total}")
        return total

    def display(self):
        ele = []
        curr = self.head
        while curr.next != None:
            curr = curr.next
            ele.append(curr.data)
        print(ele)

    def get(self, index):
        if index >= self.length():
            print("Error")
            return None
        curr_indx = 0
        curr_node = self.head
        while True:
            curr_node = curr_node.next
            if curr_indx == index: return curr_node.data
            curr_indx += 1
        



my_list = Linked_list()
my_list.linked_append(1)
my_list.linked_append(2)
my_list.linked_append(3)
my_list.linked_append(4)

my_list.display()
print(my_list.get(2))