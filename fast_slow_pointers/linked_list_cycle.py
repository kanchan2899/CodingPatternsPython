class LinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_head(self, node: LinkedListNode):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

    def get_length(self):
        temp = self.head
        length = 0

        while temp:
            length += 1
            temp = temp.next
        return length

    def get_node(self, position):
        if position != -1:
            p = 0
            ptr = self.head

            while p < position:
                ptr = ptr.next
                p += 1
            return ptr

    def __str__(self):
        result = ""
        temp = self.head
        while temp:
            result += str(temp.data)
            temp = temp.next
            if temp:
                result += ", "
        result += ""
        return result


def detect_cycle(head):
    if head is None:
        return False

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # if there's a cycle, slow and fast pointers will be same
        if slow == fast:
            return True

    return False


def main():
    inputs = [2, 4, 6, 8, 10, 12, 2]
    linked_list = LinkedList()
    linked_list.create_linked_list(inputs)

    print(detect_cycle(linked_list.head))


if __name__ == "__main__":
    main()
