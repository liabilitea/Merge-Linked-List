class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(list1, list2):
    dummy = ListNode()
    current = dummy

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            current.next = ListNode(list1.value)
            list1 = list1.next
        else:
            current.next = ListNode(list2.value)
            list2 = list2.next
        current = current.next

    if list1 is not None:
        current.next = list1
    elif list2 is not None:
        current.next = list2

    return dummy.next

def print_list(node):
    if not node:
        return
    
    print(node.value, end="")

    node = node.next
    while node:
        print(" ->", node.value, end="")
        node = node.next

    print()

def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

raw_list1_values = input("Enter values for the first list (space or comma-separated): ")
list1_values = [int(x) for x in raw_list1_values.replace(',', ' ').split()]

raw_list2_values = input("Enter values for the second list (space or comma-separated): ")
list2_values = [int(x) for x in raw_list2_values.replace(',', ' ').split()]

list1_values.sort()
list2_values.sort()

list1 = create_linked_list(list1_values)
list2 = create_linked_list(list2_values)

merged_list = merge_sorted_lists(list1, list2)
print("Merged List:", end=" ")
print_list(merged_list)
