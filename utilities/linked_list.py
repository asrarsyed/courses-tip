# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'ListNode({self.val})'


def generateLinkedList(array):
    if not array:
        return None
    head = ListNode(array[0])
    current = head
    for i in range(1, len(array)):
        current.next = ListNode(array[i])
        current = current.next
    return head


def displayLinkedList(head):
    if not head:
        print('None')
        return
    node = head
    ll = f'{node.val}'
    while node.next:
        node = node.next
        ll += f' --> {node.val}'
    print(ll)
