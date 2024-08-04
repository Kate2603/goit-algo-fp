class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        self.head = self.merge_sort(self.head)

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        def split_list(head):
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge(left, right):
            dummy = Node(0)
            current = dummy
            while left and right:
                if left.value <= right.value:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                current = current.next
            current.next = left or right
            return dummy.next

        left_half, right_half = split_list(head)
        left_sorted = self.merge_sort(left_half)
        right_sorted = self.merge_sort(right_half)
        return merge(left_sorted, right_sorted)

    def merge(self, other_list):
        self.head = self.merge_sorted_lists(self.head, other_list.head)

    def merge_sorted_lists(self, l1, l2):
        dummy = Node(0)
        current = dummy

        while l1 and l2:
            if l1.value <= l2.value:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2
        return dummy.next

# Приклад використання
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)
list1.sort()  # Список вже відсортований

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)
list2.sort()  # Список вже відсортований

# Об'єднання двох списків
merged_list = LinkedList()
merged_list.head = merged_list.merge_sorted_lists(list1.head, list2.head)

# Виведення результату
print("List 1:")
list1.print_list()
print("List 2:")
list2.print_list()
print("Merged List:")
merged_list.print_list()
