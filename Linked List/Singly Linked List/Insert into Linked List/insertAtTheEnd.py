from linkedList import Node
import printLinkedList

def insertAtTheEnd(head, key):
    if head == Node:
        return Node(head)
    current = head
    while current.next != None:
        current = current.next
    current.next = Node(key)
    return head

def main():
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(20)
    node5 = Node(60)
    node6 = Node(10)
    node7 = Node(5)
    node8 = Node(10)

    # linking Nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8

    insertAtTheEnd(node1, 200)
    printLinkedList.printList(node1)

if __name__ == '__main__':
    main()