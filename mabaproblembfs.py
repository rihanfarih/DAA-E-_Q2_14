# Maba Problem - find shortest path using BFS algorithm
# 05111940000026 - Fais Rafli Akbar Hidya  
# 05111940000159 - Salman Damai Alfariq
# 05111940000165 - Rihan Farih Bunyamin

graph = {
        'Dormnitory': ['Library', 'Manarul', 'mathematics'],
        'Library': ['Manarul', 'IS', 'ftk', 'Dormnitory'],
        'mathematics': ['Dormnitory', 'electrical'],
        'Manarul': ['Dormnitory', 'Library'],
        'IS': ['Library', 'Informatics'],
        'electrical': ['mathematics', 'bloku'],
        'bloku': ['Rescen', 'ftk', 'electrical'],
        'ftk': ['bloku', 'Library', 'Rescen'],
        'Rescen': ['bloku', 'ftk', 'Informatics'],
        'Informatics': ['IS', 'Rescen'],
        }
# IS = information System , manarul = Manarul Ilmi , electrical =  electrical engineering , FTK = Naval Technology 
# bloku =  U-block , rescen = Research Center

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
           
            

def cost(path):
    distance = {
        'Dormnitory': ['Library', 'Manarul', 'mathematics', 850, 700, 400],
        'Library': ['Manarul', 'IS', 'ftk', 'Dormnitory', 400, 170, 180, 850],
        'mathematics': ['Dormnitory', 'electrical', 550, 210],
        'Manarul': ['Dormnitory', 'Library', 700, 400],
        'IS': ['Library', 'Informatics', 170, 240],
        'electrical': ['mathematics', 'bloku', 210, 450],
        'bloku': ['Rescen', 'ftk', 'electrical', 500, 400, 450],
        'ftk': ['bloku', 'Library', 'Rescen', 400, 180, 140],
        'Rescen': ['bloku', 'ftk', 'Informatics', 500, 140, 160],
        'Informatics': ['infosys', 'Rescen', 240, 160],
    }

    cost_km = 0

    for city in range(len(path)-1):
        next_city_idx = distance[path[city]].index(path[city+1])
        x = len(distance[path[city]])
        cost_km += distance[path[city]][int(x/2) + next_city_idx]

    return cost_km

shortest_path = bfs(graph, 'Dormnitory', 'Informatics')
step_cost = cost(shortest_path)

print ("Length of Path: ", (len(shortest_path)-1))
print("The Sortest Path is:",shortest_path)
print("Step Cost:" ,step_cost,"meters")



