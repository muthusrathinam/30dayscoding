def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))
    