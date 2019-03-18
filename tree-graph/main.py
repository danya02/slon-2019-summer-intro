#!/usr/bin/python3
import bs4
import json
document = bs4.BeautifulSoup('<g></g>', features="html.parser")
root = document.g

def add_node(parent):
    node = document.new_tag('circle', cx=0, cy=0, r=10)
    parent.append(node)
    return node

def add_link(parent, node1, node2):
    link = document.new_tag('line', style='stroke:rgb(0,0,0);stroke-width:2', x1=node1['cx'], y1=node1['cy'], x2=node2['cx'], y2=node2['cy'])
    parent.append(link)

def add_transform_group(parent, x,y):
    node = document.new_tag('g', transform=f'translate({x} {y})')
    parent.append(node)
    return node

def get_tree_depth(tree):
    if len(tree)==0:return 1
    return max([get_tree_depth(child) for child in tree])+1

def create_tree(nodes, transient_root, distance_to_bottom):
    rootnode = add_node(transient_root)
    children = [(add_node(rootnode), i) for i in nodes]
    entry = -1
    current_x = 0
    max_width = 0
    for child, subtree in children:
        entry+=1
        child['cy'] += 50
        child['cx'] = current_x
        add_link(transient_root, rootnode, child)
        group = add_transform_group(transient_root, child['cx'],child['cy'])
        new_width = create_tree(subtree, group, distance_to_bottom-1)
        current_x+=new_width
        max_width = max(max_width,new_width)
    return max(max_width, entry*20*distance_to_bottom, 25)

tree = json.loads(input())
width = create_tree(tree, root, get_tree_depth(tree))

true_document = bs4.BeautifulSoup(f'<svg transform="translate(30 30)" width="{int(width*1.6)}" height="{get_tree_depth(tree)*50+30}"></svg>', features="html.parser")
true_root = true_document.svg
true_root.append(document)

print(true_document)
