class Node:
    def __init__(self, value=None,nextNode=None,previousNode=None):
        self.value=value
        self.nextNode=nextNode
        self.previousNode=previousNode

class DoublyLinkedList:
    def __init__(self,node=None):
        self.head=node
        self.size=0
    def print_list(self):
        head =self.head
        while head:
            print(f"The value is {head.value}")
            head=head.nextNode

    def addNodeTop(self,value):
        newNode=Node(value)
        newNode.nextNode=self.head
        head=self.head
        if head :
            head.previousNode=newNode
        self.head=newNode
        self.size+=1
    def addNodeBottom(self,value):
        newNode=Node(value)
        if self.head==None:
            self.addNodeTop(value)
            return
        head=self.head
        while head:
            previous=head
            head=head.nextNode
        previous.nextNode=newNode
        newNode.previousNode=previous
        self.size+=1
    def delete(self,value):
        head=self.head
        previous=None
        while head:
            if head.value==value:
                if previous is None:
                    self.head=head.nextNode
                    self.head.previousNode=None
                else:
                    previous.nextNode=head.nextNode
                    head.nextNode=previous
                    return
            else:
                previous=head
                head=head.nextNode
    def search(self,val):
        head=self.head
        while head:
            if head.value==val:
                return head
            else:
                head=head.nextNode
    def replaceNodeValue(self,newVal,val):
        node=self.search(val)
        node.value=newVal
    def reverseList(self):
        head=self.head
        previous=None
        while head:
            temp_head=head
            head=head.nextNode
            temp_head.nextNode=previous
            temp_head.previousNode=head
            previous=temp_head
        self.head=previous