""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check(node, max_val = float('inf'), min_val = float('-inf')):
    if not node:
        return True
    if node.data <= min_val or node.data >= max_val:
        return False
    return check(node.left, node.data, min_val) and check(node.right, max_val, node.data)

def check_binary_search_tree_(root):
    return check(root) 
  
  # https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees
