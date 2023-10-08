class ListNode:
        def __init__(self, val, key):
            self.val = val
            self.prev, self.next = [None] * 2
            self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.tail = ListNode(0, 0)
        self.head = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # head -> <- tail

        self.hashmap = dict()
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.hashmap: return -1
        
        # To maintain the priorities
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev, node.next = [None] * 2

        self.tail.prev.next = node
        node.prev = self.tail.prev
        self.tail.prev = node
        node.next = self.tail

        return self.hashmap[key].val


        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].val = value
            node = self.hashmap[key]
            node.prev.next = node.next
            node.next.prev = node.prev

            node.prev, node.next = [None] * 2

            self.tail.prev.next = node
            node.prev = self.tail.prev
            self.tail.prev = node
            node.next = self.tail
            return None

        node = ListNode(value, key)
        self.hashmap[key] = node


        if self.size == self.capacity:
            del self.hashmap[self.head.next.key]
            temp = self.head.next

            self.head.next = temp.next
            temp.next.prev = self.head

            del temp

            
            self.tail.prev.next = node
            node.prev = self.tail.prev

            self.tail.prev = node
            node.next = self.tail

            return None



        self.tail.prev.next = node
        node.prev = self.tail.prev

        self.tail.prev = node
        node.next = self.tail
        
        self.size += 1
        