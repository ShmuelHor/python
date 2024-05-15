class Node:
    def __init__(self,vel):
        self.data = vel
        self.next = None
        self.previoes = None
class dubelLinkList:
    head =None
    tail = None
    def insert_first(self,vel):
        new_node = Node(vel)
        if self.head != None:
            new_node.next = self.head
            self.head.previoes = new_node
        else:
            self.tail = new_node
        self.head = new_node
    def insert_last(self,val):
        new_node = Node(val)
        self.tail.next = new_node
        new_node.previoes = self.tail
        self.tail = new_node
    def insertByIindex(self,val,index):
        if index == 0 or self.head == None:
            self.insert_first(val)
        elif index == self.lenList() or index == -1:
            self.insert_last(val)
        elif index < -1 or index > self.lenList()-1:
            print("Error in *insertByIindex* The index ",index,"is not in the linklist")
        else:
            new_node = Node(val)
            pointer = self.head
            counter = 0
            while counter != index - 1:
                counter += 1
                pointer = pointer.next
            new_node.next = pointer.next
            pointer.next.previoes = new_node
            pointer.next = new_node
            new_node.previoes = pointer
    def deleteByIndex(self,index):
        pointer = self.head
        if index < 0 or index > self.lenList()-1:
            print("Error in *deleteByIndex* The index ", index, "is not in the linklist")
        elif index == 0:
                pointer = pointer.next
                pointer.previoes = None
                self.head = pointer
        else:
            counter = 0
            while counter != index - 1:
                counter += 1
                pointer = pointer.next
            if pointer.next.next == None:
                pointer.next = None
                self.tail = pointer.next
            else:
                pointer.next = pointer.next.next
                pointer.next.previoes = pointer
    def deleteByVal(self,val):
        counter = 0
        pointer = self.head
        if val == pointer.data:
            pointer = pointer.next
            pointer.previoes = None
            self.head = pointer
            return
        elif self.tail.data == val:
            self.tail.previoes.next = None
            return
        while counter != self.lenList()-1:
            if val == pointer.next.data:
                    pointer.next = pointer.next.next
                    return
            else:
                pointer = pointer.next
                counter += 1
        print("Error in *deleteByVal* The val ",val,"is not in the linklist")
    def lenList(self):
        counter = 0
        pointer = self.head
        while pointer.next != None:
            pointer = pointer.next
            counter += 1
        counter += 1
        return counter
    def print(self):
        pointer = self.head
        while pointer.next != None:
            print(pointer.data)
            pointer = pointer.next
        print(pointer.data)
aa = dubelLinkList()
aa.insertByIindex(6,0)
aa.insertByIindex(5,0)
aa.insertByIindex(4,0)
aa.insertByIindex(3,0)
aa.insertByIindex(2,0)
aa.insertByIindex(1,0)
aa.insertByIindex(7,-1)
aa.insertByIindex(9,2)
aa.insertByIindex(10,30)
aa.deleteByIndex(-1)
print("len of the linklist is: ",aa.lenList())
# aa.deleteByVal(7)
aa.print()