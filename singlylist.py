# Define a Node
class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


# Define a single linked list


class SLL:
    def __init__(self, head=None):
        self.head = head

# bool value empty list then True otherwise Fasle
    def is_empty(self):
        return self.head == None


# insertion for starting


    def insert_at_start(self, data):
        newNode = Node(data, self.head)
        self.head = newNode


# insertion for ending list


    def insert_at_end(self, data):
        newNode = Node(data)
        if not self.is_empty():
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
        else:
            self.head = newNode

# search method
    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

# insert after method
    def insert_after(self, temp, data):
        if temp is not None:
            newNode = Node(data, temp.next)
            temp.next = newNode

# print list all the element
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

# Delete first
    def delete_start(self):
        if self.head is not None:
            self.head = self.head.next

# delete last
    def delete_end(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
# delete given item

    def delete_after(self, data):
        if self.head is None:
            pass
        elif self.head.next is None and self.head.item == data:
            self.head = None
        else:
            temp = self.head
            if temp.item == data:
                self.head = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next
# iterator  given iterable

    def __iter__(self):
        return SSLIterable(self.head)
# create SSL iterable


class SSLIterable:
    def __init__(self, head):
        self.curr = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.curr:
            raise StopIteration
        data = self.curr.item
        self.curr = self.curr.next
        return data


# driver code
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_end(30)
mylist.insert_at_start(35)
mylist.insert_after(mylist.search(20), 40)
mylist.print_list()
# mylist.delete_after(30)
# mylist.delete_start()
mylist.delete_end()
print()
mylist.print_list()
print()
for x in mylist:
    print(x)
