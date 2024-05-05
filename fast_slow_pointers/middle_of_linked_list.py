from linked_list_cycle import LinkedList, LinkedListNode


def get_middle_of_ll(head: LinkedListNode):
    slow: LinkedListNode = head
    fast: LinkedListNode = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def main():
    inputs = [2, 4, 6, 8, 10, 12]
    linked_list = LinkedList()
    linked_list.create_linked_list(inputs)

    print(get_middle_of_ll(linked_list.head).data)


if __name__ == "__main__":
    main()
