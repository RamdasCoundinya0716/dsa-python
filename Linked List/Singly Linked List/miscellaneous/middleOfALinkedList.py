from linkedList import Node


def findMiddle(head):
    # Naive Approach -------> time complexity O(N) [Two traversals]
    # if head == None:
    #     return
    # count = 0
    # current = head
    # while current:
    #     current = current.next
    #     count += 1
    # current = head
    # for i in range(count // 2):
    #     current = current.next
    # print(current.data)

    # Efficient Approach using "FAST" and "SLOW" pointers

    if head == None:
        return
    fast, slow = head,head
    while fast != None and fast.next != None:
        slow, fast = slow.next, fast.next.next
    print(slow.data)


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

    findMiddle(node1)

if __name__ == '__main__':
    main()