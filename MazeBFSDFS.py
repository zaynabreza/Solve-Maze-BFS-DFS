
import sys
#Initial skeleton of code taken from lab manual provided in AI Lab

array = [[False for i in range(12)] for j in range(12)] #array to maintain visited points


def move_left(state):
    #print("Moving from ", state)
    new_state = [row[:] for row in state]
    
    indexi=-1
    for i, e in enumerate(new_state):
        try:
            indexj=e.index(2)
            indexi=i               
        except ValueError:
            pass
    
    if indexj not in [0] and new_state[indexi][indexj-1]==1:
        new_state[indexi][indexj]=1
        new_state[indexi][indexj-1]=2        
        return new_state
    else:
        return None
    
    


def move_right(state):
    new_state = [row[:] for row in state]
    
    indexi=-1
    for i, e in enumerate(new_state):
        try:
            indexj=e.index(2)
            indexi=i               
        except ValueError:
            pass
    
    if indexj not in [11] and new_state[indexi][indexj+1]==1:
        new_state[indexi][indexj]=1
        new_state[indexi][indexj+1]=2        
        return new_state
    else:
        return None


def move_up(state):
    new_state = [row[:] for row in state]
    
    indexi=-1
    for i, e in enumerate(new_state):
        try:
            indexj=e.index(2)
            indexi=i               
        except ValueError:
            pass
    
    if indexi not in [0] and new_state[indexi-1][indexj]==1:
        new_state[indexi][indexj]=1
        new_state[indexi-1][indexj]=2        
        return new_state
    else:
        return None


def move_down(state):
    
    new_state = [row[:] for row in state]
    
    indexi=-1
    for i, e in enumerate(new_state):
        try:
            indexj=e.index(2)
            indexi=i               
        except ValueError:
            pass
    
    if indexi not in [11] and new_state[indexi+1][indexj]==1:
        new_state[indexi][indexj]=1
        new_state[indexi+1][indexj]=2        
        return new_state
    else:
        return None


def create_node(state, parent, operator, depth):
    return Node(state, parent, operator, depth)


def expand_node(node,nodes,goal):
  expanded_nodes = []  
  global direct
  up = move_up(node.state)
  if up != None: #moving up is allowed from state

      x=create_node(up, node.state, "up", node.depth+1)
    
      for i, e in enumerate(up):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass

      if array[indexi][indexj] != True: #if hasnt been visited before                    
        expanded_nodes.append(x) 
  
  left = move_left(node.state)
  if left != None: #moving left is allowed from state
 
      x=create_node(left, node.state, "left", node.depth+1)
      for i, e in enumerate(left):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass
      if array[indexi][indexj] != True:          
        expanded_nodes.append(x) 

  right = move_right(node.state) 
  if right != None: #moving right is allowed from state
     
      x=create_node(right, node.state, "right", node.depth+1)
      #x.print()
      for i, e in enumerate(right):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass
      if array[indexi][indexj] != True:       
        expanded_nodes.append(x) 

  down = move_down(node.state)
  if down != None: #moving down is allowed from state
    
      x=create_node(down, node.state, "down", node.depth+1)
      #x.print()
      for i, e in enumerate(down):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass
      if array[indexi][indexj] != True:
        expanded_nodes.append(x)   
      
  return expanded_nodes

def equals(a, b):
  isEqual=True
  for i in range (0,12):
    for j in range (0,12):
      if a[i][j]!=b[i][j]:
        isEqual=False
        return isEqual
  return isEqual

def bfs(start, goal):

    visited_nodes = []
    nodes = []
    nodes_expanded = 0
    global array
    array = [[False for i in range(12)] for j in range(12)]
    steps=0
    global direct
    direct=0
    result=[None]
    matches=True
    nodes.append(create_node(start, None, None, 0))

    while nodes:
        current_node = nodes.pop(0)     


        visited_nodes.append(current_node)

        for i, e in enumerate(current_node.state):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass

        array[indexi][indexj] = True

        #print("Current node is ",indexj,",", indexi)

        
        #print("Step ",steps)            


        if current_node.state == goal:
          #print("Result complete")
          print("***************************************")
          print("Direct Path Cost: ", current_node.depth)          
          return steps

        steps+=1
        exp_ans = expand_node(current_node, nodes,goal)

        if exp_ans == 0:
          return steps
        else:
          for node in exp_ans:
            if node not in visited_nodes:
              nodes.append(node)
            elif node in visited_nodes:
              direct-=1


        
                    

def dfs(start, goal):

    visited_nodes = []
    nodes = []
    nodes_expanded = 0
    global array
    array = [[False for i in range(12)] for j in range(12)]
    steps=0
    global repeats
    repeats=0
    result=[None]
    matches=True
    nodes.append(create_node(start, None, None, 0))

    while nodes:
        current_node = nodes.pop()  
        visited_nodes.append(current_node)

        for i, e in enumerate(current_node.state):
          try:
              indexj=e.index(2)
              indexi=i               
          except ValueError:
              pass

        array[indexi][indexj] = True

        #print("Current node is ",indexj,",", indexi)

       
        
        #print("Step ",steps)   


        if current_node.state == goal:
          #print("Result complete")
          print("***************************************")
          print("Direct Path Cost: ", current_node.depth)          
          return steps

        steps+=1
        exp_ans = expand_node(current_node, nodes,goal)

        if exp_ans == 0:
          return steps
        else:   
          for node in reversed(exp_ans):
            if node not in visited_nodes:
              nodes.append(node)
            else:
              repeats=repeats+1


class Node:
    def __init__(self, state, parent, operator, depth):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth=depth

    def print(self):
      print("State: ", self.state, "Parent: ", self.parent, "Operator: ", self.operator)
        
def print_array(a):
  for i in range (0,12):
        for j in range (0,12):
            print(a[i][j]," ", end = '')
        print("\n")

def main():

    maze=[[0,0,0,0,0,0,0,0,0,0,0,0],
          [0,1,1,1,0,1,1,1,1,1,1,0],
          [0,1,0,1,0,1,0,0,0,0,1,0],
          [0,0,0,1,0,1,1,1,1,0,1,0],
          [0,1,1,1,1,0,0,0,1,0,1,1],
          [0,0,0,0,1,0,1,0,1,0,1,0],
          [0,1,1,0,1,0,1,0,1,0,1,0],
          [0,0,1,0,1,0,1,0,1,0,1,0],
          [0,1,1,1,1,1,1,1,1,0,1,0],
          [0,0,0,0,0,0,1,0,0,0,1,0],
          [1,1,1,1,1,1,1,0,1,1,1,0],
          [0,0,0,0,0,0,0,0,0,0,0,0]]

    startpoint="4,11"
    endpoint="10,0"
 
    starting_state= [row[:] for row in maze]
    indices=startpoint.split(",")
    starting_state[int(indices[0])][int(indices[1])]=2
    
   
    goal_state = [row[:] for row in maze]
    indices=endpoint.split(",")
    goal_state[int(indices[0])][int(indices[1])]=2
    
    
    print("_________    Printing start state _________")
    
    print_array(starting_state)

    print("_________    Printing goal state _________")

    print_array(goal_state)
    

    result = bfs(starting_state, goal_state)
    print("ALgorithm Used= BFS")
    print("No of Moves Utilized: ",result)

    print("***************************************")
    result = dfs(starting_state, goal_state)
    print("ALgorithm Used= DFS")
    print("No of Moves Utilized: ",result)
    print("***************************************")
     


if __name__ == "__main__":
    main()



