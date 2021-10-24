class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children = []

    @property
    def identifier(self):
        return self.__identifier

    @property
    def children(self):
        return self.__children

    def add_child(self, node):
        self.__children.append(node)
        
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
        
    def display(self):
        self.doDisplay(0)
    
    def doDisplay(self, depth):
        print("\t"*depth + str(self))
        depth += 1
        for child in self.children:
            child.doDisplay(depth)  # recursive call
          
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
        
