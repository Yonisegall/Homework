###################################### ---Q1B--- ######################################
from BinarySearchTree import *
from DNA import *


def complement_BST_DNA(sequence_BST):
    """
    The function receives a binary search tree representing a DNA strand. Each node in the tree consists of a positive
    integer type key representing the position of the nucleotide in the strand, and a value of type string representing
    the single nucleotide in the vertex. The function returns A string, representing the complementary strand in
    reverse order.
    :param sequence_BST: Binary search tree
    :return: A string representing the complementary strand in  reverse order.
    """
    lst = sequence_BST.inorder()
    strand = ""
    for tup in lst:
        strand += tup[1]
    DNA_strand = DNA(strand)
    return str(DNA_strand.complement())


########### Tests ############
BST = BinarySearchTree()
BST.insert(4, "T")
BST.insert(2, "A")
BST.insert(6, "C")
BST.insert(1, "G")
BST.insert(3, "A")
BST.insert(7, "G")
BST.insert(5, "T")
print(BST)
print(complement_BST_DNA(BST))
print(BST.inorder())
print(BST.preorder())
