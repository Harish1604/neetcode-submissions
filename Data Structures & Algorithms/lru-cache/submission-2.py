class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next= None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head =  Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    
    def removeNode(self,node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def moveFront(self,node):
        self.removeNode(node)
        self.addNode(node)
    
    def poptail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node           

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.moveFront(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.moveFront(node)
            return
        
        newNode = Node(key,value)
        self.cache[key] = newNode
        self.addNode(newNode)

        if len(self.cache) > self.capacity:
             node = self.poptail()
             del self.cache[node.key]
                
