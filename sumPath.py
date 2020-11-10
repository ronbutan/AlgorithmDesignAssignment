from typing import List
# 112. Path Sum
'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumPath(root,sum):
    if root is None:
        return False

    ## Handle the leaf case
    if root.left is None and root.right is None:
        if sum == root.val:
            return True
        else:
            return False
    else:
        return sumPath(root.left, sum - root.val) or sumPath(root.right, sum - root.val)
    
    

# node1 = TreeNode(7,None,None)
# node2 = TreeNode(2,None,None)
# node3 = TreeNode(5,None,None)
# node4 = TreeNode(1,None,None)
# node5 = TreeNode(11,node1,node2)
# node6 = TreeNode(13,None,None)
# node7 = TreeNode(4,node3,node4)
# node8 = TreeNode(4,node5,None)
# node9 = TreeNode(8,node6,node7)
# # node2 = TreeNode(-3,None,None)

# root = TreeNode(5,node8,node9)
# #print(sumPath(root,-5))


# 113. Path Sum II
'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
'''

def tailPathSum(root, cumul, sum, l):
    if root is None:
        return

    ## Handle the leaf case
    if root.left is None and root.right is None:
        if sum == root.val:
            cumul = cumul + str(root.val)
            l.append([int(x) for x in cumul.split('+')])
            return
    else:
        cumul = cumul + str(root.val) + "+"
        tailPathSum(root.left, cumul, sum - root.val, l)
        tailPathSum(root.right, cumul, sum - root.val, l)
def pathSum(root,sum):
    if not root:
        return []

    l = []
    tailPathSum(root,'',sum, l)
    print(l)

node1 = TreeNode(7,None,None)
node2 = TreeNode(2,None,None)
node3 = TreeNode(5,None,None)
node4 = TreeNode(1,None,None)
node5 = TreeNode(11,node1,node2)
node6 = TreeNode(13,None,None)
node7 = TreeNode(4,node3,node4)
node8 = TreeNode(4,node5,None)
node9 = TreeNode(8,node6,node7)

root = TreeNode(5,node8,node9)


node1 = TreeNode(-3,None,None)
node2 = TreeNode(None,None,None)
root = TreeNode(-2,node1,node2)

#root = TreeNode(1,None,None)
pathSum(root, -5)