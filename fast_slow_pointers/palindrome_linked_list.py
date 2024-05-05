from linked_list_cycle import LinkedList, LinkedListNode


def reverse_linked_list(slow):
    prev_node = None
    next_node = None
    current_node = slow

    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node


def compare_two_halves(first_half, second_half):
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        else:
            first_half = first_half.next
            second_half = second_half.next
    return True


def is_palindrome(head):
    slow: LinkedListNode = head
    fast: LinkedListNode = head

    # find the middle of linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half of the linked list starting from the middle node

    revert_data = reverse_linked_list(slow)

    # compare the first half and second half of linked list after reversing the second half
    check = compare_two_halves(head, revert_data)

    # re-reverse the second half of the linked list to restore the original linked list
    reverse_linked_list(revert_data)

    if check:
        return True

    return False


def main():
    ll = [9, 7, 4, 4, 7, 9]
    linked_list = LinkedList()
    linked_list.create_linked_list(ll)
    head = linked_list.head

    print(is_palindrome(head))


if __name__ == "__main__":
    main()
