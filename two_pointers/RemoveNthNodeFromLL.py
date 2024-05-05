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

    # create  linked list method will create the linked list using the given integer array
    # with the help of insert_at_head method
    def create_linked_list(self, lst):
        for x in reversed(lst):
            new_node = LinkedListNode(x)
            self.insert_node_at_head(new_node)

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


def print_list(ll_node: LinkedListNode):
    temp = ll_node
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

        if temp:
            print("->", end=" ")
        else:
            print("-> null", end=" ")


def remove_nth_last_element(head, n):
    right = head
    left = head

    for i in range(n):
        right = right.next

    if not right:
        return head.next

    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next
    return head


def main():
    lists = [[23, 89, 19, 9, 8, 7], [4, 1, 2, 3, 6]]
    n = [3, 4]
    for i in range(len(n)):
        input_linked_list = LinkedList()
        input_linked_list.create_linked_list(lists[i])
        print_list(input_linked_list.head)
        res = remove_nth_last_element(input_linked_list.head, n[i])
        print_list(res)
        print()


if __name__ == "__main__":
    main()
