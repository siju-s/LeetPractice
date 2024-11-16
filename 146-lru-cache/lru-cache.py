class ListNode(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # Map of int key and value will be ListNode
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head        
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        # remove from front 
        node = self.cache[key]
        self.remove(node)
        # add to back
        self.add(node)
        return node.val    
        

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        newNode = ListNode(key, value)
        self.add(newNode)
        self.cache[key] = newNode
        if len(self.cache) > self.capacity:
            del_node = self.head.next
            self.remove(del_node)
            del self.cache[del_node.key]


    def add(self, newNode):
        actualTail = self.tail.prev
        actualTail.next = newNode

        newNode.prev = actualTail
        newNode.next = self.tail
        self.tail.prev = newNode

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)