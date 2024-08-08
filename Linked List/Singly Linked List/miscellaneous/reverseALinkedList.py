from linkedList import Node
from printLinkedList import printList

def reverseList(head):
    # Naive Approach

    # stack = []
    # current = head
    # while current:
    #     stack.append(current)
    #     current = current.next
    # current = head
    # while current is not None:
    #     current.data = stack.pop()
    #     current = current.next
    # return head.data

    #------------------------------------------------------------------------------------------

    # Efficient Approach
    prev = None
    current = head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move prev and current one step forward
        current = next_node
    return prev  # prev will be the new head of the reversed list



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

    printList(node1)  # Before reversal
    reversed_head = reverseList(node1)
    printList(reversed_head)  # After reversal

if __name__ == '__main__':
    main()