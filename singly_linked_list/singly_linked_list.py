class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def add_to_tail(self, value):
        node = ListNode(value)
        self.length += 1
        # if head does not exist, set both head and tail to the node that you created.
        if self.head is None:
            self.head = node
            self.tail = node
        # if head exists
        else:
            # set previous tail next pointer from None to node that you created.
            self.tail.next = node
            # set the list tail to the node you created.
            self.tail = node

    def add_to_head(self, value):
        node = ListNode(value)
        self.length += 1
        # check to see if there is a head (Is the list empty right now?)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            # take node that I'm creating and point the next pointer to the current head
            node.next = self.head
            # tell the linked list that the inserted node is the new head
            self.head = node

    def contains(self, value):
        current_node = self.head
        
        while current_node is not None:
            if current_node.value == value:
                return True
            
            current_node = current_node.next

        return False

    def remove_head(self):
        # update self.head pointer
        if self.head is not None:
            cur_val = self.head
            self.head = self.head.next
            if self.head is None: # checking to see if we have removed the last node
                self.tail = None
            self.length -= 1
            return cur_val.value
        else:
            return None

    def get_max(self):
        if self.head is None:
            return None

        node = self.head
        incr = 0
        value = 0

        while incr < self.length:
            incr += 1
            if value < node.value:
                value = node.value
            node = node.next
        return value

