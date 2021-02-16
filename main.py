from doubly_linked_list import DoublyLinkedList
def main():
    print("Thi is running !")
    listt= DoublyLinkedList()
    listt.addNodeBottom(1)
    listt.addNodeBottom(2)
    listt.addNodeBottom(3)
    listt.addNodeBottom(4)
    listt.reverseList()
    #sprint(listt.head.nextNode.previousNode.value)

    #print(listt.head.nextNode.nextNode.previousNode.previousNode.value)
    listt.print_list()

if __name__=="__main__":
    main()