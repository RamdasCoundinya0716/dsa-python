from linkedList import Node
from printLinkedList import printList

def sortedInsert(head, key):
    newNode = Node(key)
    # Insert at the start if the new key is smaller than the head's data
    if head is None or head.data >= key:
        newNode.next = head
        return newNode
    
    # Traverse the list to find the insertion point
    current = head
    while current.next and current.next.data < key:
        current = current.next
    
    # Insert new node after 'current'
    newNode.next = current.next
    current.next = newNode
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

    # Linking Nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8

    # Insert new node in sorted order
    sorted_list = sortedInsert(node1, 40)
    printList(sorted_list)

if __name__ == '__main__':
    main()