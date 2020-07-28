class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorderTraversal(root):
    if root is not None:
        print(root.data, end=" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)


def postorderTraversal(root):
    if root is not None:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.data, end=" ")


def levelorderTraversal(root):
    import queue
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        curr = q.get()
        print(curr.data, end=" ")
        if curr.left:
            q.put(curr.left)
        if curr.right:
            q.put(curr.right)
        
def inorderTraversal(root):
    if root is not None:
        inorderTraversal(root.left)
        print(root.data, end=" ")
        inorderTraversal(root.right)

tree = TreeNode("1")
tree.left = TreeNode("2")
tree.right = TreeNode("3")
tree.left.left = TreeNode("4")
tree.left.left.left = TreeNode("8")
tree.left.right = TreeNode("5")
tree.right.left = TreeNode("6")
tree.right.left.left = TreeNode("9")
tree.right.left.right = TreeNode("10")
tree.right.right = TreeNode("7")

"""
        1
      /   \
     2     3
    /\     /\
   4  5   6  7
  /      /\
 8      9 10

"""

print("PREORDER TRAVERSAL")
preorderTraversal(tree)
print("\n")

print("POSTORDER TRAVERSAL")
postorderTraversal(tree)
print("\n")

print("LEVELORDER TRAVERSAL")
levelorderTraversal(tree)
print("\n")

print("INORDER TRAVERSAL")
inorderTraversal(tree)
print("\n")
