class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def insert(node, key):
  if node is None:
    return Node(key)
  if key < node.value:
    node.left = insert(node.left, key)
  else:
    node.right = insert(node.right, key)
  return node

def lowestCommonAncestor(node, source, destination):
  if node is None:
    return None
  if node.value == source or node.value == destination:
    return node

  if source < node.value and destination < node.value:
    return LCA(node.left, source, destination)
  elif source > node.value and destination > node.value:
    return LCA(node.right, source, destination)
  return node
  
def distance(node, source, destination):
  def getLevel(node, key, level: int) -> int:
    if node is None:
      return -1
    if node.value == key:
      return level
  
    if key < node.value:
      return getLevel(node.left, key, level+1)
    elif key > node.value:
      return getLevel(node.right, key, level+1)

  ancestor = lowestCommonAncestor(node, source, destination)
  distanceFromSource: int = getLevel(ancestor, source, 0)
  distanceFromDestination: int = getLevel(ancestor, destination, 0)
  totalDistance = distanceFromSource + distanceFromDestination
  return totalDistance

def main():
  values = [int(value) for value in input().split()]
  root = None
  for value in values:
    root = insert(root, value)
  
  source, destination = input().split()
  
  print(distance(root, int(source), int(destination)))

if __name__ == "__main__":
  main()
