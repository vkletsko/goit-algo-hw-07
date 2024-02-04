import graphviz


class BinaryTree:
    class Node:
        def __init__(self, key, data=None, left_node=None, right_node=None):
            self.key = key
            self.data = data
            self.left_node = left_node
            self.right_node = right_node

        def __str__(self):
            return str(self.key)

    def __init__(self):
        self.root = None

    def add(self, key, data=Node):
        def _add(key, data, node):
            if node is None:
                return BinaryTree.Node(key, data)
            if node.key == key:
                node.data = data
            if node.key > key:
                node.left_node = _add(key, data, node.left_node)
            else:
                node.right_node = _add(key, data, node.right_node)
            return node

        self.root = _add(key, data, self.root)

    def get(self, key):
        def _get(key, node):
            if node is None:
                return None
            if node.key == key:
                return node.data
            if node.key > key:
                return _get(key, node.left_node)
            else:
                return _get(key, node.right_node)

        return _get(key, self.root)

    # Task1
    def find_biggest_node(self):
        def _find_biggest_node(node):
            if node.right_node is None:
                return node.key
            return _find_biggest_node(node.right_node)

        return _find_biggest_node(self.root)

    # Task2
    def find_smallest_node(self):
        def _find_smallest_node(node):
            if node.left_node is None:
                return node.key
            return _find_smallest_node(node.left_node)

        return _find_smallest_node(self.root)

    # Task3
    def sum(self):
        def _sum(node):
            if node is None:
                return 0
            return _sum(node.left_node) + node.key + _sum(node.right_node)

        return _sum(self.root)


def visualize_binary_tree(btree):
    dot = graphviz.Digraph()
    dot.node(str(btree.root.key))

    def add_nodes_edges(node):
        if node.left_node:
            dot.node(str(node.left_node.key))
            dot.edge(str(node.key), str(node.left_node.key))
            add_nodes_edges(node.left_node)
        if node.right_node:
            dot.node(str(node.right_node.key))
            dot.edge(str(node.key), str(node.right_node.key))
            add_nodes_edges(node.right_node)

    add_nodes_edges(btree.root)
    dot.render('doc/binary_tree', view=True, format='pdf')


# Find the smallest and the biggest node
b_tree = BinaryTree()

b_tree.add(8, "Lion")
b_tree.add(6, "Tiger")
b_tree.add(5, "Jaguar")
b_tree.add(10, "Cheetah")
b_tree.add(9, "Lynx")
b_tree.add(7, "Leopard")
b_tree.add(0, "Jungle cat")  # The smallest key
b_tree.add(13, "Puma")  # The biggest key


# Output
print("Showing the tree as pdf autput: doc/binary_tree.pdf")
visualize_binary_tree(b_tree)
print("The sum of the keys of the vertices:", b_tree.sum())
print("Smallest node:", b_tree.find_smallest_node())
print("Biggest node:", b_tree.find_biggest_node())
