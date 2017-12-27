import math

## Get the shortest path using A* search algorithm
##
## based on wikipedia article
##
##

def shortest_path(M,start,goal):
    print("shortest path called, Start", start, "Goal", goal)
    
    #the set already explored
    closedSet = set()
    
    #only the start node is known
    openSet = {start}
    
    #the dictionary with the parent with the best way until the node
    cameFrom = dict()
    
    #cost of getting from the start to the node
    gScore = dict()
    gScore[start] = 0
    
    fScore = dict()
    #the straight line distance between start and goal
    fScore[start] = distance(M.intersections[start], M.intersections[goal])
    
    while openSet:
        current = node_lowest_value(openSet, fScore)
        
        # If reached the goal, YEAH!
        if current == goal:
            print("Goal Reached!")
            return reconstruct_path(cameFrom, current)
        
        openSet.remove(current) #remove from open
        closedSet.add(current) #mark as processed
                
        for neighbor in M.roads[current]:
            if neighbor in closedSet:
                continue
            
            #add the neighbor to the frontier
            openSet.add(neighbor)
                
            #The distance from start to a neighbor
            tentative_gScore = gScore[current] + distance(M.intersections[current], M.intersections[neighbor])
            if neighbor in gScore: 
                if tentative_gScore >= gScore[neighbor]:
                    continue # This is not a better path.
            
            # This path is the best until now. Record it!
            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + distance(M.intersections[neighbor], M.intersections[goal])
        
    return
        
def reconstruct_path(cameFrom, current):
    total_path = list()
    total_path.insert(0,current)
    while current in cameFrom:
        current = cameFrom[current]
        total_path.insert(0 , current)
    return total_path
    
def node_lowest_value(openSet, fScore):
    lowest_node = 35767 #large number
    lowest_value = float('inf')
    for node in fScore:
        if fScore[node] < lowest_value:
            if node in openSet:
                lowest_node = node
                lowest_value = fScore[node]
    return lowest_node

def distance(p1,p2):
    distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
    return distance