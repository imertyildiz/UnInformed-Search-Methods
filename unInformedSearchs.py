class Node:
    def __init__(self, name):
        self.name = name
        self.path = [name]
        self.parentNode = ''
        self.depth = 0
        self.cost = 0


# Expand Function of BFS
def expandBFS(graph, node):
    successors = []
    for i in graph[node.name]:
        s = Node(i[0])
        s.parentNode = node.name
        s.depth = node.depth + 1
        s.path = node.path.copy()
        s.path.append(s.name)
        s.cost = node.cost + (i[1])
        successors.append(s)
    return successors


# Function of BFS
def bfs(graph, startNode, endNode):
    track = [startNode]
    fringe = [Node(startNode)]
    while fringe:
        node = fringe.pop(0)
        for i in expandBFS(graph, node):
            if i.name == endNode:
                fringe.append(i)
                track.append(i.name)
                result = (i.path, track, i.depth)
                return result
            fringe.append(i)
            if track[-1] != endNode:
                track.append(i.name)
    return None


# Expand Function of DLS
def dlsExpand(graph, node):
    successors = []
    for i in graph[node.name]:
        s = Node(i[0])
        s.parentNode = node.name
        s.depth = node.depth + 1
        s.path = node.path.copy()
        s.path.append(s.name)
        s.cost = node.cost + (i[1])
        successors.insert(0, s)
    return successors


# Function of Recursive function of DLS
def dlsRecursive(graph, startNode, endNode, maximum_depth_limit, node, track):
    track.append(node.name)
    if node.name == endNode:
        return (node.path, track, node.depth)
    elif maximum_depth_limit == node.depth:
        return None
    else:
        for i in dlsExpand(graph, node):
            result = dlsRecursive(graph, startNode, endNode, maximum_depth_limit, i, track)
            if result != None:
                return result
        return None


# Function of DLS
def dls(graph, startNode, endNode, maximum_depth_limit):
    track = []
    return dlsRecursive(graph, startNode, endNode, maximum_depth_limit, Node(startNode), track)


# Function of IDDFS
def iddfs(graph, startNode, endNode, maximum_depth_limit):
    for i in range(0, maximum_depth_limit + 1):
        result = dls(graph, startNode, endNode, i)
        if result != None:
            return result
    return None


# Expand Function of UCS
def expandUCS(graph, node):
    successors = []
    for i in graph[node.name]:
        s = Node(i[0])
        s.parentNode = node.name
        s.depth = node.depth + 1
        s.path = node.path.copy()
        s.path.append(s.name)
        s.cost = node.cost + (i[1])
        successors.append(s)
    return successors


# Function of UCS
def ucs(graph, startNode, endNode):
    track = []
    fringe = [Node(startNode)]
    while fringe:
        node = fringe.pop(0)
        track.append(node.name)
        if node.name == endNode:
            result = (node.path, track, node.depth, node.cost)
            return result
        for i in expandUCS(graph, node):
            for j in fringe:
                if i.name == j.name and i.cost < j.cost:
                    j.cost = i.cost
                    j.depth = i.depth
                    j.path = i.path.copy()
                    j.parentNode = i.parentNode
                break
            fringe.append(i)
        fringe.sort(key=lambda x: x.cost)
    return None


# Whole definition of UnInformedSearch
def UnInformedSearch(method_name, problem_file_name, maximum_depth_limit):
    with open(problem_file_name) as f:
        lines = f.read().splitlines()
    graph = {}
    startNode = lines.pop(0)
    endNode = lines.pop(0)
    found1 = True
    found2 = True
    for line in lines:
        found1 = True
        found2 = True
        listOfLine = line.split(' ')
        if listOfLine[0] in graph:
            for i in graph[listOfLine[0]]:
                if i[0] == listOfLine[1]:
                    i[1] = int(listOfLine[2])
                    found1 = False
            if found1:
                graph[listOfLine[0]].append([listOfLine[1], int(listOfLine[2])])
        else:
            graph[listOfLine[0]] = [[listOfLine[1], int(listOfLine[2])]]
        if listOfLine[1] in graph:
            for i in graph[listOfLine[1]]:
                if i[0] == listOfLine[0]:
                    i[1] = int(listOfLine[2])
                    found2 = False
            if found2:
                graph[listOfLine[1]].append([listOfLine[0], int(listOfLine[2])])
        else:
            graph[listOfLine[1]] = [[listOfLine[0], int(listOfLine[2])]]
    if method_name == "BFS":
        return bfs(graph, startNode, endNode)
    elif method_name == "DLS":
        return dls(graph, startNode, endNode, maximum_depth_limit)
    elif method_name == "IDDFS":
        return iddfs(graph, startNode, endNode, maximum_depth_limit)
    elif method_name == "UCS":
        return ucs(graph, startNode, endNode)
