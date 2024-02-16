def printree(t, bykey=True):
    """Print a textual representation of t
    bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
    bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)  # + ": " + str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
    a root node, its left node, and its right node
    root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "\\" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


###################################### ---Q3A--- ######################################
class BinaryDecisionTreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.key) + ":" + str(self.val)

    def is_leaf(self):
        """The method returns True or False, whether the node is a leaf or not"""
        if self.left is None and self.right is None:
            return True
        else:
            return False


###################################### ---Q3B--- ######################################
class BinaryDecisionTree:
    def __init__(self, elements):
        self.root = BinaryDecisionTreeNode(0, elements[0])
        lst_of_nodes = [self.root]
        for i in range(1, len(elements)):
            if lst_of_nodes[0].left is None:
                lst_of_nodes[0].left = BinaryDecisionTreeNode(i, elements[i])
                lst_of_nodes.append(lst_of_nodes[0].left)
            elif lst_of_nodes[0].right is None:
                lst_of_nodes[0].right = BinaryDecisionTreeNode(i, elements[i])
                lst_of_nodes.append(lst_of_nodes[0].right)
                lst_of_nodes = lst_of_nodes[1:]

    def __repr__(self):
        # no need to understand the implementation of this one
        out = ""
        # need printree.py file or make sure to run it in the NB
        for row in printree(self.root):
            out = out + row + "\n"
        return out

###################################### ---Q3C--- ######################################
    def decide(self, input_value):
        """The method returns as a string the path of the value down the tree represented
         by the chain of keys of the vertices where the input passed"""
        way = ""
        node = self.root
        way += f'{node.key}'
        while not node.is_leaf():
            if node.val(input_value):
                node = node.left
                way += f'->{node.key}'
            else:
                node = node.right
                way += f'->{node.key}'
        return way

###################################### ---Q3D--- ######################################
    def output(self, input_value):
        """The method returns the result of the execution of that function above
         the value given as input. Otherwise, the method will return None"""
        node = self.root
        while not node.is_leaf():
            if node.val(input_value):
                node = node.left
            else:
                node = node.right
        value = node.val(input_value)
        if isinstance(value, bool):
            return None
        else:
            return value

###################################### ---Q3E--- ######################################
    def compact(self):
        """The method returns a nested list in each list lambda functions according
         to the distance from the root of the tree according to the index"""
        node = self.root
        lst_nodes = [node]
        lst_root = [node]
        lst_values = [node.val]
        lst_tree = [lst_values]
        lst_values = []
        while len(lst_nodes) != 0:
            while len(lst_root) != 0:
                if lst_root[0].left is not None:
                    lst_nodes.append(lst_root[0].left)
                if lst_root[0].right is not None:
                    lst_nodes.append(lst_root[0].right)
                lst_root = lst_root[1:]
                lst_nodes = lst_nodes[1:]
            for i in lst_nodes:
                lst_root.append(i)
                lst_values.append(i.val)
            if len(lst_root) != 0:
                lst_tree.append(lst_values)
                lst_values = []
        return lst_tree


###################### Test ######################

############### Test_1 ################
lambda_elements_1 = [lambda x: x % 2 == 0, lambda x: x % 3 == 0, lambda x: x % 4 == 0, lambda x: x % 6 == 0,
                     lambda x: x // 20 == 9, lambda x: x % 8 == 0, lambda x: x % 3]
D_tree_1 = BinaryDecisionTree(lambda_elements_1)
print(D_tree_1)
print(D_tree_1.compact()[2][1](20))
print(D_tree_1.output(60))
print(D_tree_1.output(9))
print(D_tree_1.decide(12))

############### Test_2 ################
lambda_elements_2 = [lambda x: len(x) >= 4, lambda x: x.upper() == x, lambda x: x.capitalize() == x,
                     lambda x: x.startswith("A"), lambda x: "I am " + x, lambda x: x.endswith("t")]
D_tree_2 = BinaryDecisionTree(lambda_elements_2)
print(D_tree_2)
print(D_tree_2.decide("Esraa"))
print(D_tree_2.decide("Tom"))
print(D_tree_2.output("Assaf"))
print(D_tree_2.output("Tom"))
print(D_tree_2.compact()[2][0]("Noy"))
