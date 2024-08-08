from linkedList import Node
from printLinkedList import printList

def nThNodeFromEnd(head, n):
    if head == None:
        return None
    first = head
    for i in range(n):
        if first == None:
            return
        first = first.next
    second = head
    while first:
        second = second.next
        first = first.next
    return second

def main():
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(40)
    node5 = Node(50)
    node6 = Node(60)
    node7 = Node(70)
    node8 = Node(80)

    # linking Nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8

    targetNode = nThNodeFromEnd(node1, 6)
    print(targetNode.data)

if __name__ == '__main__':
    main()