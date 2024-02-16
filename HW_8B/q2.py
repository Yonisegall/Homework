###################################### ---Q2--- ######################################
from BinaryTree import *


def print_right_view(binary_tree):
    """
    The function receives a binary tree in which each vertex contains a key and a value. The function returns a list
    containing the values The rightmost vertices in each set of vertices at a certain distance from the root
    :param binary_tree: Binary tree.
    :return: A list with the rightmost values in each row in the tree
    """
    root = binary_tree.root
    lst_right_nodes = [root.val]
    lst_nodes = []
    lst_node_front = [root]
    while len(lst_node_front) != 0:
        node = lst_node_front[0]
        if node.right is not None:
            lst_nodes.append(node.right)
        if node.left is not None:
            lst_nodes.append(node.left)
        lst_node_front = lst_node_front[1:]
        if len(lst_node_front) == 0:
            if len(lst_nodes) == 0:
                continue
            lst_right_nodes.append(lst_nodes[0].val)
            lst_node_front = lst_nodes
            lst_nodes = []
    return lst_right_nodes


################### Tests ####################

############## Test_1 ################
bin_tree = BinaryTree()
n1 = TreeNode(1, 'a')
n2 = TreeNode(2, 'b')
n3 = TreeNode(3, 'c')
n4 = TreeNode(4, 'd')
n5 = TreeNode(5, 'e')
n6 = TreeNode(6, 'f')
bin_tree.root = n6
n6.left = n3
n6.right = n2
n2.right = n4
n3.left = n1
n3.right = n5
print(bin_tree)
print(print_right_view(bin_tree))


############## Test_2 ################
bin_tree = BinaryTree()
n1 = TreeNode(1, 'a')
n2 = TreeNode(2, 'b')
n3 = TreeNode(3, 'c')
n4 = TreeNode(4, 'd')
n5 = TreeNode(5, 'e')
n6 = TreeNode(6, 'f')
n7 = TreeNode(12, 'x')
n8 = TreeNode(23, 'y')
bin_tree.root = n6
n6.left = n3
n6.right = n2
n2.right = n4
n3.left = n1
n3.right = n5
n5.left = n7
n1.right = n8
print(bin_tree)
print(print_right_view(bin_tree))

############### Test_3 ################
print(f'Question 2\n')
bin_tree = BinaryTree()
n1 = TreeNode(1, 'a')
n2 = TreeNode(2, 'b')
n3 = TreeNode(3, 'c')
n4 = TreeNode(4, 'd')
n5 = TreeNode(5, 'e')
n6 = TreeNode(6, 'f')
bin_tree.root = n6
n6.left = n3
n6.right = n2
n2.right = n4
n3.left = n1
n3.right = n5
print(bin_tree)
print(print_right_view(bin_tree))
print(print_right_view(bin_tree) == ["f", "b", "d"])


############### Test_4 ################
bin_tree = BinaryTree()
n1 = TreeNode(1, 'a')
n2 = TreeNode(2, 'b')
n3 = TreeNode(3, 'c')
n4 = TreeNode(4, 'd')
n5 = TreeNode(5, 'e')
n6 = TreeNode(6, 'f')
n7 = TreeNode(12, 'x')
n8 = TreeNode(23, 'y')
bin_tree.root = n6
n6.left = n3
n6.right = n2
n2.right = n4
n3.left = n1
n3.right = n5
n5.left = n7
n1.right = n8
print(bin_tree)
print(print_right_view(bin_tree))
print(print_right_view(bin_tree) == ["f", "b", "d", "x"])

############### Test_5 ################
bin_tree = BinaryTree()
n1 = TreeNode(1, 'a')
n2 = TreeNode(2, 'b')
n3 = TreeNode(3, 'c')
n4 = TreeNode(4, 'd')
n5 = TreeNode(5, 'e')
n6 = TreeNode(6, 'f')
n7 = TreeNode(12, 'x')
n8 = TreeNode(23, 'y')
n9 = TreeNode(45, 'I')
n10 = TreeNode(30, 'R')
bin_tree.root = n6
n6.left = n3
n6.right = n2
n2.right = n4
n3.left = n1
n3.right = n5
n5.left = n7
n1.right = n8
n4.right = n9
n8.left = n10
print(bin_tree)
print(print_right_view(bin_tree))
print(print_right_view(bin_tree) == ["f", "b", "d", "I", "R"])
print()

############### Test_6 ################
bin_tree = BinaryTree()
n1 = TreeNode(1, 'a')
n2 = TreeNode(2, 'b')
n3 = TreeNode(3, 'c')
n4 = TreeNode(4, 'd')
n5 = TreeNode(5, 'e')
n6 = TreeNode(6, 'f')
n7 = TreeNode(12, 'x')
n8 = TreeNode(23, 'y')
n9 = TreeNode(45, 'q')
n10 = TreeNode(99, 'm')
bin_tree.root = n6
n6.left = n3
n6.right = n2
n2.right = n4
n3.left = n1
n3.right = n5
n5.left = n7
n1.right = n8
n7.left = n9
n9.right = n10
print(bin_tree)
print(print_right_view(bin_tree))
print(print_right_view(bin_tree) == ["f", "b", "d", "x", "q", "m"])

############### Test_7 ################
bin_tree = BinaryTree()
n1 = TreeNode(1, 'a')
n2 = TreeNode(2, 'b')
n3 = TreeNode(3, 'c')
n4 = TreeNode(4, 'd')
n5 = TreeNode(5, 'e')
n6 = TreeNode(6, 'f')
n7 = TreeNode(12, 'x')
n8 = TreeNode(23, 'y')
n9 = TreeNode(45, 'I')
n10 = TreeNode(30, 'R')
bin_tree.root = n6
n6.left = n3
n6.right = n2
n2.right = n4
n3.left = n1
n3.right = n5
n5.left = n7
n1.right = n8
n4.right = n9
n8.left = n10
print(bin_tree)
print(print_right_view(bin_tree))
print(print_right_view(bin_tree) == ["f", "b", "d", "I", "R"])
print()

############### Test_8 ################
bin_tree = BinaryTree()
n1 = TreeNode(1, 'a')
n2 = TreeNode(2, 'b')
n3 = TreeNode(3, 'c')
n4 = TreeNode(4, 'd')
n5 = TreeNode(5, 'e')
n6 = TreeNode(6, 'f')
n7 = TreeNode(12, 'x')
n8 = TreeNode(23, 'y')
n9 = TreeNode(45, 'q')
n10 = TreeNode(99, 'm')
bin_tree.root = n6
n6.left = n3
n6.right = n2
n2.right = n4
n3.left = n1
n3.right = n5
n5.left = n7
n1.right = n8
n7.left = n9
n9.right = n10
print(bin_tree)
print(print_right_view(bin_tree))
print(print_right_view(bin_tree) == ["f", "b", "d", "x", "q", "m"])

############### Test_9 ################
bin_tree = BinaryTree()
n1 = TreeNode(1, 'a')
n2 = TreeNode(2, 'b')
n3 = TreeNode(3, 'c')
n4 = TreeNode(4, 'd')
n5 = TreeNode(5, 'e')
n6 = TreeNode(6, 'f')
n7 = TreeNode(12, 'x')
n8 = TreeNode(23, 'y')
n9 = TreeNode(45, 'q')
n10 = TreeNode(99, 'm')
n11 = TreeNode(98, '@')
n12 = TreeNode(97, '#')
n13 = TreeNode(96, '$')
n14 = TreeNode(95, '&')
n15 = TreeNode(94, '!')
n16 = TreeNode(93, 'N')
n17 = TreeNode(93, 'Q')
bin_tree.root = n6
n6.left = n3
n6.right = n2
n2.right = n4
n3.left = n1
n3.right = n5
n5.left = n7
n1.right = n8
n7.left = n9
n9.right = n10
n10.right = n11
n10.left = n14
n11.left = n12
n11.right = n13
n12.left = n15
n15.right = n16
n15.left = n17
print(bin_tree)
print(print_right_view(bin_tree))
print(print_right_view(bin_tree) == ["f", "b", "d", "x", "q", "m", "@", "$", "!", "N"])
print("\n" * 3)