# I used the the "number of misplaced tiles" as heuristic function for my AStar implementation of 8Puzzle
# I used the "sum of the distances of the tiles from their goal positions (manhattan distance)" as heuristic function for my AStar implementation of Maze

# Node Class
class Node:
    def __init__(self, name):
        self.name = name
        self.path = []
        self.parentNode = ''
        self.depth = 0
        self.cost = 0
        self.costTotal = 0


# number of misplaced tiles function
def countOfDifference(string1, string2):
    i = 0
    count = 0
    while i < 9:
        if string1[i] == ' ':
            i += 1
            continue
        if string1[i] != string2[i]:
            count += 1
        i += 1
    return count


# Expand Function for Puzzle for both UCS and ASTAR
def expandPuzzle(node, finalString, isUcsOrAstar):
    successors = []
    possibleWays = ["LEFT", "UP", "RIGHT", "DOWN"]
    for i in possibleWays:
        if i == "LEFT":
            x = node.name.find(' ')
            if x == 0 or x == 3 or x == 6:
                continue
            else:
                s = Node(node.name)
                tmp = node.name[x - 1]
                s.name = s.name.replace(' ', tmp)
                s.name = s.name.replace(tmp, ' ', 1)
                s.parentNode = node.name
                s.depth = node.depth + 1
                s.path = node.path.copy()
                s.path.append("LEFT")
                if isUcsOrAstar:  # if == 1 then AStar
                    s.cost = node.cost + 1
                    s.costTotal = s.cost + countOfDifference(s.name, finalString)
                else:
                    s.costTotal = node.costTotal + 1
                successors.append(s)
        elif i == "UP":
            x = node.name.find(' ')
            if x == 0 or x == 1 or x == 2:
                continue
            else:
                s = Node(node.name)
                tmp = node.name[x - 3]
                s.name = s.name.replace(' ', tmp)
                s.name = s.name.replace(tmp, ' ', 1)
                s.parentNode = node.name
                s.depth = node.depth + 1
                s.path = node.path.copy()
                s.path.append("UP")
                if isUcsOrAstar:  # if == 1 then AStar
                    s.cost = node.cost + 1
                    s.costTotal = s.cost + countOfDifference(s.name, finalString)
                else:
                    s.costTotal = node.costTotal + 1
                successors.append(s)
        elif i == "RIGHT":
            x = node.name.find(' ')
            if x == 2 or x == 5 or x == 8:
                continue
            else:
                s = Node(node.name)
                tmp = node.name[x + 1]
                s.name = s.name.replace(tmp, ' ')
                s.name = s.name.replace(' ', tmp, 1)
                s.parentNode = node.name
                s.depth = node.depth + 1
                s.path = node.path.copy()
                s.path.append("RIGHT")
                if isUcsOrAstar:  # if == 1 then AStar
                    s.cost = node.cost + 1
                    s.costTotal = s.cost + countOfDifference(s.name, finalString)
                else:
                    s.costTotal = node.costTotal + 1
                successors.append(s)
        else:
            x = node.name.find(' ')
            if x == 6 or x == 7 or x == 8:
                continue
            else:
                s = Node(node.name)
                tmp = node.name[x + 3]
                s.name = s.name.replace(tmp, ' ')
                s.name = s.name.replace(' ', tmp, 1)
                s.parentNode = node.name
                s.depth = node.depth + 1
                s.path = node.path.copy()
                s.path.append("DOWN")
                if isUcsOrAstar:  # if == 1 then AStar
                    s.cost = node.cost + 1
                    s.costTotal = s.cost + countOfDifference(s.name, finalString)
                else:
                    s.costTotal = node.costTotal + 1
                successors.append(s)
    return successors


# Expand Function for Maze for both UCS and ASTAR
def expandMaze(node, maze, mazeWidth, mazeHeight, isUcsOrAstar, solutionString):
    successors = []
    possibleWays = ["LEFT", "UP", "RIGHT", "DOWN"]
    for i in possibleWays:
        if i == "LEFT":
            if node.name[0] != 0 and maze[node.name[0] + node.name[1] * mazeWidth - 1] != '#':
                s = Node(node.name)
                s.name = (s.name[0] - 1, s.name[1])
                s.parentNode = node.name
                s.depth = node.depth + 1
                s.path = node.path.copy()
                s.path.append(s.name)
                if isUcsOrAstar:  # ASTAR
                    s.cost = node.cost + 1
                    s.costTotal = s.cost + abs(solutionString[0] - s.name[0]) + abs(
                        solutionString[1] - s.name[1])
                else:
                    s.costTotal = node.costTotal + 1
                successors.append(s)
            else:
                continue
        elif i == "UP":
            if node.name[1] != 0 and maze[node.name[0] + (node.name[1] - 1) * mazeWidth] != '#':
                s = Node(node.name)
                s.name = (s.name[0], s.name[1] - 1)
                s.parentNode = node.name
                s.depth = node.depth + 1
                s.path = node.path.copy()
                s.path.append(s.name)
                if isUcsOrAstar:  # ASTAR
                    s.cost = node.cost + 1
                    s.costTotal = s.cost + abs(solutionString[0] - s.name[0]) + abs(
                        solutionString[1] - s.name[1])
                else:
                    s.costTotal = node.costTotal + 1
                successors.append(s)
            else:
                continue
        elif i == "RIGHT":
            if node.name[0] != (mazeWidth - 1) and maze[node.name[0] + node.name[1] * mazeWidth + 1] != '#':
                s = Node(node.name)
                s.name = (s.name[0] + 1, s.name[1])
                s.parentNode = node.name
                s.depth = node.depth + 1
                s.path = node.path.copy()
                s.path.append(s.name)
                if isUcsOrAstar:  # ASTAR
                    s.cost = node.cost + 1
                    s.costTotal = s.cost + abs(solutionString[0] - s.name[0]) + abs(
                        solutionString[1] - s.name[1])
                else:
                    s.costTotal = node.costTotal + 1
                successors.append(s)
            else:
                continue
        else:
            if node.name[1] != (mazeHeight - 1) and maze[node.name[0] + (node.name[1] + 1) * mazeWidth] != '#':
                s = Node(node.name)
                s.name = (s.name[0], s.name[1] + 1)
                s.parentNode = node.name
                s.depth = node.depth + 1
                s.path = node.path.copy()
                s.path.append(s.name)
                if isUcsOrAstar:  # ASTAR
                    s.cost = node.cost + 1
                    s.costTotal = s.cost + abs(solutionString[0] - s.name[0]) + abs(
                        solutionString[1] - s.name[1])
                else:
                    s.costTotal = node.costTotal + 1
                successors.append(s)
            else:
                continue
    return successors


# General Expand Function for Maze and Puzzle
def expandUCS(node, isMazeOrPuzzle, maze, mazeWidth, mazeHeight, isUcsOrAstar, solutionString):
    # isMazeOrPuzzle = 1 (PUZZLE)
    if isMazeOrPuzzle:
        return expandPuzzle(node, solutionString, isUcsOrAstar)
    # isMazeOrPuzzle = 0 (MAZE)
    else:
        if node.path == []:
            node.path.append(node.name)
        return expandMaze(node, maze, mazeWidth, mazeHeight, isUcsOrAstar, tuple(solutionString))


# General Function of Maze and 8Puzzle
def ucs(initialString, solutionString, isMazeOrPuzzle, maze, mazeWidth, mazeHeight, isUcsOrAstar):
    closed = []
    track = []
    fringe = [Node(initialString)]
    while fringe:
        node = fringe.pop(0)
        track.append(node.name)
        if node.name == solutionString:
            result = (node.path, track, node.depth, node.depth)
            return result
        if node.name not in closed:
            closed.append(node.name)
            for i in expandUCS(node, isMazeOrPuzzle, maze, mazeWidth, mazeHeight, isUcsOrAstar, solutionString):
                fringe.append(i)
        fringe.sort(key=lambda x: x.costTotal)

    return None


def InformedSearch(method_name, problem_file_name):
    with open(problem_file_name) as f:
        lines = f.read().splitlines()
    # Number of lines of puzzle is 7. So this is equal to "if maze:"
    # For MAZE
    if len(lines) > 7:
        initial = lines.pop(0)
        initial = initial[1:-1]
        initial = initial.split(',')
        initial[0] = int(initial[0])
        initial[1] = int(initial[1])
        final = lines.pop(0)
        final = final[1:-1]
        final = final.split(',')
        final[0] = int(final[0])
        final[1] = int(final[1])
        # First element of the initial is x of starting and second is y. As in final.
        mazeWidth = len(lines[0])
        mazeHeight = len(lines)
        maze = ""
        for i in lines:
            maze += i
        if method_name == "UCS":
            return ucs(tuple(initial), tuple(final), 0, maze, mazeWidth, mazeHeight, 0)
        elif method_name == "AStar":
            return ucs(tuple(initial), tuple(final), 0, maze, mazeWidth, mazeHeight,
                       1)  # is UcsOrAstar = 1 so it is Astar
    # For PUZZLE
    else:
        initial = lines.pop(0).split(' ')
        initial += lines.pop(0).split(' ')
        initial += lines.pop(0).split(' ')
        lines.pop(0)
        final = lines.pop(0).split(' ')
        final += lines.pop(0).split(' ')
        final += lines.pop(0).split(' ')
        initialPuzzle = ''.join(map(str, initial))
        initialPuzzle = initialPuzzle.replace('0', ' ')
        finalPuzzle = ''.join(map(str, final))
        finalPuzzle = finalPuzzle.replace('0', ' ')
        if method_name == "UCS":
            return ucs(initialPuzzle, finalPuzzle, 1, 0, 0, 0, 0)
        elif method_name == "AStar":
            return ucs(initialPuzzle, finalPuzzle, 1, 0, 0, 0, 1)
