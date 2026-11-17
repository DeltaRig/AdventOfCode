# Nov 2026
# Daniela Rigoli

import sys
from tracemalloc import start
from datetime import datetime

# Definition for a binary tree node - get from Leetcode
class TreeNode:
    def __init__(self, val="0", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Qual a altura da árvore binária descrita
class Solution:
    def readFile(self, filename):
        with open(filename, 'r') as f:
            lines = [line.split() for line in f]
        return lines

    def createBT(self, lines):
        if not lines:
            return None
        return self._createBT(lines, 0, 0, len(lines[0])-1)
        

    def _createBT(self, lines, a, c,qt):
        print("|a: ", a, " c: ", c, " qt: ", qt)
        if qt <= 0:
            return None
        if qt == 1:
            return TreeNode(lines[0][a])
        print("a: ", a, " c: ", c, " qt: ", qt)
        print("lines[0][a]: ", lines[0][a])
        # find the index of the root in the inorder traversal
        root = TreeNode(lines[0][a])
        print("root: ", root.val)
        index = lines[1].index(lines[0][a]) # root at inorder
        print("index: ", index)
        root.left = self._createBT(lines, a+1, c, index-c)
        root.right = self._createBT(lines, a+index-c+1, index+1, qt-1-index+c)
        return root

    def height(self, lines):
        if not lines:
            return -1
        return self._height(lines, 0, 0, len(lines[0])-1)
        
    
    def _height(self, lines, a, c,qt):
        if qt <= 0:
            return 0
        if qt == 1:
            return 0
        
        index = lines[1].index(lines[0][a]) # find the index of the root in the inorder traversal
        l = self._height(lines, a+1, c, index-c)
        r = self._height(lines, a+index-c+1, index+1, qt-1-index+c)
        return max(r, l) + 1

    def __str__(self, root, level=0):
        if not root:
            return ""
        ret = "\t"*level + str(root.val) + "\n"
        if root.left:
            ret += "L" +self.__str__(root.left, level+1)
        if root.right:
            ret += "R" + self.__str__(root.right, level+1)
        return ret

# read file and create tree
solution = Solution()
# from terminal input the file name as argument
if len(sys.argv) < 2:
    print("Please provide a filename as an argument.")
    sys.exit(1)

filename = sys.argv[1]
lines = solution.readFile(filename)


# start creating
# root = solution.createBT(lines) # (optional)
# print(solution.__str__(root))
start_time = datetime.now()
# start getting hight
h = solution.height(lines)
# end time
end_time = datetime.now()
print("| ", filename, " | ",format(end_time - start_time), " |",h, " |")
#print('Duration: {}'.format(end_time - start_time))
#print("height: ", h)
# print binary tree in level order
