import timeit
import numpy as np

def IDA(initial_state, goal_state):
    initial_node = Node(initial_state)
    goal_node = Node(goal_state)
    
    threshold = manhattan_heuristic(initial_state, goal_state)
    
    print("heuristic threshold: {}".format(threshold))
    
    loop_counter = 0

    while 1:
        path = set([initial_node])
        
        tmp = search(initial_node, goal_state, 0, threshold, path)
        
        print("tmp: {}".format(tmp))
        if tmp == True:
            return True, threshold
        elif tmp == float('inf'):
            return False, float('inf')
        else:
            threshold = tmp


def search(node, goal_state, g, threshold, path):
    #print("node-state: {}".format(node.state))
    f = g + manhattan_heuristic(node.state, goal_state)

    if f > threshold:
        return f

    if np.array_equal(node.state, goal_state):
        return True

    minimum = float('inf')  
    for n in node.nextnodes():
        if n not in path:
            path.add(n)
            tmp = search(n, goal_state, g + 1, threshold, path)
            if tmp == True:
                return True
            if tmp < minimum:
                minimum = tmp

    return minimum


def manhattan_heuristic(state1, state2):
    size = range(1, len(state1) ** 2)
    distances = [count_distance(num, state1, state2) for num in size]

    return sum(distances)


def count_distance(number, state1, state2):
    position1 = np.where(state1 == number)
    position2 = np.where(state2 == number)

    return manhattan_distance(position1, position2)


def manhattan_distance(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


class Node():
    def __init__(self, state):
        self.state = state
    
    def __repr__(self):
        return np.array_str(self.state.flatten())

    def __hash__(self):
        return hash(self.__repr__())
        
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def nextnodes(self):
        zero = np.where(self.state == 0)
        
        y,x = zero
        y = int(y)
        x = int(x)
        
        up = (y - 1, x) 
        down = (y + 1, x)
        right = (y, x + 1)
        left = (y, x - 1)

        arr = []
        for direction in (up, down, right, left):
            if len(self.state) - 1 >= direction[0] >= 0 and len(self.state) - 1 >= direction[1] >= 0:
                tmp = np.copy(self.state)
                tmp[direction[0], direction[1]], tmp[zero] = tmp[zero], tmp[direction[0], direction[1]]
                arr.append(Node(tmp))

        return arr


initial_state = np.array([[8, 7, 3],[4, 1, 2],[0, 5, 6]])
goal_state = np.array([[1, 2, 3],[8, 0, 4],[7, 6, 5]])

start = timeit.default_timer()
is_found, th = IDA(initial_state, goal_state)
stop = timeit.default_timer()

print('Time: {} seconds'.format(stop - start))

if is_found is True:
    print("Solution found with heuristic-upperbound: {}".format(th))
else:
    print("Solution not found!")

