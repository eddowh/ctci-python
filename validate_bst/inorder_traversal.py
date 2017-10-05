# -*- coding: utf-8 -*-

""" Node is defined as
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

prev = None


def checkBST(root):
    global prev

    # In-order traversal:
    # -------------------
    # RF = recursive function
    # foo = do something
    #
    #   RF(root.left)
    #   foo(root.data)
    #   RF(root.right)
    if root is not None:
        # cannot just return checkBST(root.left) here
        # if left child is valid, then return True will stop here
        if not checkBST(root.left):
            return False

        # foo:
        # - set prev to root
        if prev is not None and prev.data >= root.data:
            return False
        prev = root

        # return because all other conditions have been checked
        return checkBST(root.right)

    # root is None -> valid
    return True
