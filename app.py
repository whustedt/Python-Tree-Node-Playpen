from node import Node
import random

def createTree(shuffle=False, addExtra=False):
    root = Node('root')
    
    role1 = Node('role1')
    srum = Node('srum')
    his = Node('his')
    role2 = Node('role2')
    clearing = Node('clearing')
    role3 = Node('role3')
    leben = Node('leben')
    moped = Node('moped')
    
    root.add_child(role1)
    role1.add_child(srum)
    srum.add_child(his)
    
    root.add_child(role2)
    role2.add_child(clearing)
    
    root.add_child(role3)
    role3.add_child(leben)
    role3.add_child(moped)
    
    if (addExtra):
        his.add_child(Node('partner'))
    
    if (shuffle):
        [random.shuffle(child.children) for child in root.traverse()]
    
    return root

def debugDump(name, tree, detailed=True):
    print('*** NAME:', name)
    tree.display()
    if (detailed):
        print('***** DEPTH-FIRST ITERATION *****')
        [print(identifier) for identifier in tree.traverse()]
        print('***** BREADTH-FIRST ITERATION *****')
        [print(identifier) for identifier in tree.traverse(mode='breadth')]
        
def compare(tree1_name, tree1, tree2_name, tree2):
    print(f'{tree1_name} is {tree2_name}: {tree1 is tree2}')
    print(f'{tree1_name} == {tree2_name}: {tree1 == tree2}')
    print(f'{tree1_name} < {tree2_name}: {tree1 < tree2}')
    print(f'hash({tree1_name}): {hash(tree1)}, hash({tree2_name}): {hash(tree2)}')

tree1 = createTree()
tree2 = createTree()
tree3 = createTree(shuffle=True)
tree4 = createTree(addExtra=True)

debugDump('tree1', tree1, False)
debugDump('tree2', tree2, False)
debugDump('tree3', tree3, False)
debugDump('tree4', tree4, False)
compare('tree1', tree1, 'tree1', tree1)
compare('tree1', tree1, 'tree2', tree2)
compare('tree1', tree1, 'tree3', tree3)
compare('tree1', tree1, 'tree4', tree4)

debugDump('tree1-detailed', tree1, True)
