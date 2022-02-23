""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
# we check for max_val since every node on the right side of a node in a higher level should be higher than that higher level node
# we check for min_val since every node on the left side of a node in a higher level should be less than that higher level node
def check(node, max_val = float('inf'), min_val = float('-inf')):
    # if we made it to a None value that means we had no problems so we return true
    if not node:
        return True
    # if our data is smaller than the min_val this isn't a valid BST
    # if our data is larger than the max_val this isn't a valid BST
    if node.data <= min_val or node.data >= max_val:
        return False
    # recursively check each node's subtree for if it's part of a valid BST
    return check(node.left, node.data, min_val) and check(node.right, max_val, node.data)

def check_binary_search_tree_(root):
    return check(root) 
  
  # https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees
