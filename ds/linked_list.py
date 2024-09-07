class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, value) -> None:
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def append(self, value) -> None:
        new_node = Node(value)

        if not self.tail:
            new_node = self.head
            new_node = self.tail
            return

        # without tail
        # curr = self.head
        # while curr.next:
        #     curr = curr.next
        # curr.next = new_node

        self.tail.next = new_node
        new_node = self.tail

    def print(self) -> None:
        if not self.head:
            return

        curr = self.head
        output = ""
        while curr:
            output += f"{curr.value} -> "
            curr = curr.next
        print(output.rstrip(" -> "))

    def append_values(self, *args) -> None:
        for arg in args:
            self.append(arg)

    def __len__(self) -> int:
        curr = self.head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        return length

    def remove_at(self, index) -> None:
        """ """
        if index > len(self):
            raise ValueError("index out of range")

        if index == 0 and self.head.next:
            self.head = self.head.next
            return

        if index == 0 and self.head.next is None:
            self.head = None
            self.tail = None
            return

        if index == len(self):
            self.head = None
            return

        # count = 0
        # curr = self.head
        # while curr:
        #     if index - 1 == count:
        #         curr.next = curr.next.next
        #         break
        #     curr = curr.next
        #     count += 1

        curr = self.head
        prev = None
        while index and curr:
            prev = curr
            curr = curr.next
            index -= 1

        prev.next = curr.next

        def insert_at(self, index, value):
            pass


def main():
    ll = LinkedList()

    for i in range(10, 0, -1):
        ll.insert(i)

    ll.print()

    ll.append(11)

    ll.print()

    print(len(ll))

    ll.remove_at(2)

    ll.print()


if __name__ == "__main__":
    main()
