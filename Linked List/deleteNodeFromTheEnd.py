from linkedList import Node
from printLinkedList import printList

def deleteNodeFromTheEnd(head):
    if head is None:
        return None
    if head.next is None:
        return None  # If there's only one node, return None as the list will be empty after deletion
    
    current = head
    while current.next.next: 
        current = current.next # Traverse till the second last node

    # Now current is the second last node
    current.next = None
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

    node1 = deleteNodeFromTheEnd(node1)
    printList(node1)

if __name__ == '__main__':
    main()