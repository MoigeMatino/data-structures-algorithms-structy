def depth_first_values(root):
    stack = [root]
    values = []
    if root is None:
        return []
    while stack:
        current = stack.pop
        values.append(current)

        if current.right:
            values.append(current.right)
        if current.left:
            values.append(current.left)
