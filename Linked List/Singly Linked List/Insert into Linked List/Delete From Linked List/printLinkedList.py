from linkedList import Node

def printList(head):
    current = head
    while current:
        if current.next:
            print(f'{current.data} ->', end=' ')
        else:
            print(current.data)
        current = current.next

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

    printList(node1)

if __name__ == '__main__':
    main()