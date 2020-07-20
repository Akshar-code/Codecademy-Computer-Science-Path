# Define your "TreeNode" Python class below
class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    print("Adding " + child_node.value)
    self.children.append(child_node)
    
  def remove_child(self, child_node):
    print("Removing " + child_node.value + " from " + self.value)
    self.children = [child for child in self.children if child is not child_node]

  def traverse(self):
    print("Traversing...")
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      #nodes_to_visit.pop()
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit+=(current_node.children)
    

root = TreeNode("CEO")
first_child = TreeNode("Vice-President")
second_child = TreeNode("Head of Marketing")
third_child = TreeNode("Marketing Assistant")

root.add_child(first_child)
root.add_child(second_child)
second_child.add_child(third_child)

root.traverse()
