# Create a node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Insert a node
def insert(node, key):
    # Return a new node if the tree is empty
    if node is None:
        return Node(key)
    
    # Traverse to the right place and insert the node
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node

def LCA(node: Node, source: int, destination: int):
    if node is None:
        return None
    if node.value == source or node.value == destination:
        return node
    if source.value < node.value and destination.value < node.value:
        return LCA(node.left, source, destination)
    elif source.value > node.value and destination.value > node.value:
        return LCA(node.right, source, destination)
    return node

def distance(node: Node, source: int, destination: int):
    return