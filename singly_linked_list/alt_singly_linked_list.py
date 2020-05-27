class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def insert_after(self, value):
      current_next = self.next
      node = ListNode(value)
      
      if current_next:
        self.next = node.next
        node.next = current_next

    def insert_before(self, value):
      pass      
    
    def delete(self):
      pass


class LinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
      return self.length

    def add_to_head(self, value):
      node = ListNode(value)
      self.length += 1
      self.head = node

    def add_to_tail(self, value):
        node = ListNode(value)
        self.length += 1

        # if there is a tail
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.tail = node
            self.head = node

    def remove_head(self):
        temp = self.head.value
        self.head = self.head.next
        self.next = None
        return temp
#      head
#  1 -> 2 -> 3

    def get_max(self):
        pass

    def contains(self, value):
        if self.head == self.tail:
            return self.head.value
    
        node = self.head
        incr = 0

        while incr < self.length:
            incr += 1
            if value == node.value:
                return True
            else:
                node = node.next


