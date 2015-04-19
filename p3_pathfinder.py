from heapq import heappush, heappop
from math import sqrt

def find_path(source_point, destination_point, mesh):

    # Need to implement bidirectional, A* seems to be working

    def AStar(src, dst, graph):
        dist = {}
        prev = {}
        detail_points = {}
        queue = []
        detail_points[src] = source_point
        detail_points[dst] = destination_point
        dist[src] = 0
        prev[src] = None
        heappush(queue, (dist[src], src))

        while queue:
            _, node = heappop(queue)
            if node == dst:
                break

            neighbors = graph['adj'].get(node, []) # method from piazza
            for next_node in neighbors:
                nodePos = detail_points[node]
                nodeX, nodeY = nodePos
                nextX1, nextX2, nextY1, nextY2 = next_node
                # next box formula from piazza
                nextPos = (min(nextX2-1,max(nextX1,nodeX)), min(nextY2-1,max(nextY1,nodeY)))
                detail_points[next_node] = nextPos
                tentative = dist[node] + eucDist(detail_points[node], detail_points[next_node])
                if next_node not in dist or tentative < dist[next_node]:
                    visited_nodes.append(next_node)
                    dist[next_node] = tentative
                    prev[next_node] = node
                    heappush(queue, (tentative + eucDist(detail_points[next_node], destination_point), next_node))

        if node == dst:
            path = []
            detail_points[src] = source_point
            detail_points[dst] = destination_point
            while node:
                prevNode = prev[node]
                if prevNode is not None:
                    path.append((detail_points[node], detail_points[prevNode]))
                node = prevNode
            return path
        else:
            return []
            
    def checkBox(point, box):
        x, y = point
        x1, x2, y1, y2 = box
        if x > x1 and x <= x2 and y > y1 and y <= y2:
            return True
        else:
            return False

    def eucDist(pointA, pointB):
        x1, y1 = pointA
        x2, y2 = pointB
        return sqrt((x2-x1)**2+(y2-y1)**2)
    

    path = []
    visited_nodes = []
    start_box = None
    end_box = None
    source = False
    destination = False
    
    for box in mesh['boxes']:
        if checkBox(source_point, box):
            start_box = box
            path.append(source_point)
            source = True
        if checkBox(destination_point, box):
            end_box = box
            path.append(destination_point)
            destination = True
        if source and destination:
            break
    
    if start_box == end_box: # trivial path (same box)
        path = [(source_point,destination_point)]
        visited_nodes = [start_box]
    else:
        path = AStar(start_box, end_box, mesh)
        
    if not path:
        print "No path!"

    return (path, visited_nodes)