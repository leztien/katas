"""
Binary Tree Traversals
"""


from random import randint
from itertools import count

import matplotlib.pyplot as plt
import networkx as nx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout



class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def make_tree(depth=3, **kwargs):
    if depth == 1:
        return
    
    g = kwargs.get('counter', count())
    root = kwargs['root'] if 'root' in kwargs else Node(next(g))
    edges = kwargs['edges'] if 'edges' in kwargs else []
    full = kwargs.get('full', False)
    
    if depth == 2 and not full and randint(0,1):
        return 
    
    left = Node(next(g))
    right = Node(next(g))
    root.left, root.right = left, right
    
    edges.extend([(root.value, left.value), (root.value, right.value)])
    
    make_tree(depth - 1, root=left, counter=g, edges=edges, full=full)
    make_tree(depth - 1, root=right, counter=g, edges=edges, full=full)
    return root, edges


def draw_graph_from_edge_list(edges):
    T = nx.from_edgelist(edges)
    pos = nx.spring_layout(T)
    pos = graphviz_layout(T, prog="dot")
    
    nx.draw(T, pos, 
            with_labels=True, 
            node_size=350,
            node_color='lightgreen',
            font_size=14,
            font_weight='bold')
    plt.show()
    return T

##############################################################    


def preorder(node):
    if node is None:
        return []
    return [node.value] + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.value] + inorder(node.right) 


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.value]


def levelorder(node, depth=0, d=None):
    if node is None:
        return
    
    if depth == 0:
        d = dict()
    
    if depth not in d: d[depth] = []
    d[depth].append(node.value)
    
    levelorder(node.left, depth=depth+1, d=d)
    levelorder(node.right, depth=depth+1, d=d)
    
    if depth == 0:
        return sum([d[k] for k in sorted(d.keys())], [])


def count_levels(root, depth=0):
    """get the depth of the tree"""
    node = root
    
    if node is None:
        return depth
    
    return max(
        count_levels(node.left, depth=depth+1), 
        count_levels(node.right, depth=depth+1))
    

def count_nodes(root):
    """get the number of nodes (off by one = bug)"""
    node = root
    
    if node is None:
        return 1
    
    return sum([count_nodes(node.left), count_nodes(node.right)])
    

def count_leaves(root):
    """get the number of leaves"""
    #???
    
#########################################################
## make a random binary tree ##

root, edges = make_tree(depth=4, full=False)
T = draw_graph_from_edge_list(edges)


##################################################
## TRAVERSALS ##

l = preorder(root)
print("\npre-order:", l)

l = inorder(root)
print("\nin-order: ", l)

l = postorder(root)
print("\npost-order: ", l)

l = levelorder(root)
print("\nlevel-order: ", l)

d = count_levels(root)
print("\ntree depth =", d)

n = count_nodes(root)
print("\nnumber of nodes =", n-1)   # off-by-one bug
