class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children = []
        self.__siblings = []
        self.__parent = None

    @property
    def identifier(self):
        return self.__identifier

    @property
    def children(self):
        return self.__children
    
    @property
    def parent(self):
        return self.__parent
        
    @property
    def siblings(self):
        return self.__siblings
    
    @parent.setter
    def parent(self, value):
        self.__parent = value
    
    def is_root(self):
        return self.parent is None
    
    def is_leaf(self):
        return len(self.children) == 0
        
    def depth(self, depth=0):
        if (self.is_root()):
            return depth
        else:
            return self.parent.depth(depth+1)    
        
    def reset_siblings(self, siblings):
        self.__siblings = []
        [self.__siblings.append(sibling) for sibling in siblings if sibling!= self]
        
    def add_child(self, node):
        node.parent = self
        self.__children.append(node)
        [child.reset_siblings(self.children) for child in self.children]
        
    def __repr__(self):
        return f'Node({self.identifier})[{len(self.children)}]'

    def __str__(self):
        return self.identifier
        
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.identifier == other.identifier and sorted(self.children) == sorted(other.children)
        return False
        
    def __hash__(self):
        return hash(self.identifier)
        
    def __lt__(self, other):
        return self.identifier < other.identifier
    
    def display(self, depth=0):
        print('\t'*depth + str(self))
        depth += 1
        for child in self.children:
            child.display(depth)  # recursive call
          
    def traverse(self, mode='depth'):
        yield self
        queue = self.children
        while queue:
            yield queue[0]
            expansion = queue[0].children
            if mode == 'depth':
                queue = expansion + queue[1:]  # depth-first
            elif mode == 'breadth':
                queue = queue[1:] + expansion  # width-first
        