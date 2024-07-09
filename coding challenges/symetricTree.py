# both trees are empty return True
# root1 is None == True and root2 is None == False return False
#root1 is None == False and root2 is None == False but root1.val == root2.val == False return False

def symmetric(root1, root2):
    if root1 is None and root2 is None:
        return True
    elif ((root1 is None) != (root2 is None)) or root1.val != root2.val:
        return False
    else:
        return symmetric(root1.left, root2.right) and symmetric(root1.right, root2.left)
    
def confirm(root):
    if root is None:
        return True
    return symmetric(root.left, root.rght)