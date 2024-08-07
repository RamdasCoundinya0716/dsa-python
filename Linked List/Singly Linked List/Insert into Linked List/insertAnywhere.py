from linkedList import Node
from printLinkedList import printList

def insertNodeAnywhere(head, key, position):
    newNode = Node(key)
    # If the list is empty or position is 1 (insert at the head)
    if head is None or position == 1:
        newNode.next = head
        return newNode
    
    current = head
    for i in range(position - 2):
        '''
        Here we are using position - 2 because:
        1) The index of linked lists starts from 1.
        2) Logic : To insert a new node at position n, you need to traverse to the node currently at position n-1 
            because you need to modify the next pointer of this node to point to the new node.
        3) For eg., If you want to insert at position 3, you need to:
            i) Traverse to position 2 (one node before the target position 3).
            ii) Adjust the next pointer of the node at position 2 to point to the new node.
            iii) Set the next pointer of the new node to point to the node that was originally at position 3.
        '''
        if current is None:  # If the position is greater than the length of the list
            return head
        current = current.next

    if current is None:
        return head  # If the position is greater than the length of the list

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

    # linking Nodes
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    node7.next = node8

    head = insertNodeAnywhere(node1, 15, 3)
    printList(head)

if __name__ == "__main__":
    main()
