from heapq import heappush, heappop
from math import sqrt

def find_path(source_point, destination_point, mesh):

    def AStar(src, dst, graph):
        forward_dist = {}
        backward_dist = {}
        forward_prev = {}
        backward_prev = {}
        detail_points = {}
        queue = []
        detail_points[src] = source_point
        detail_points[dst] = destination_point
        forward_dist[src] = 0
        backward_dist[dst] = 0
        forward_prev[src] = None
        backward_prev[dst] = None
        tentative = 0
        nextDist = 0
        heappush(queue, (forward_dist[src], src, 'destination'))
        heappush(queue, (backward_dist[dst], dst, 'source'))

        while queue:
            _, node, curr_goal = heappop(queue)
            if curr_goal == 'destination' and node in backward_prev:
                break
            if curr_goal == 'source' and node in forward_prev:
                break

            neighbors = graph['adj'].get(node, []) # method from piazza
            for next_node in neighbors:
                nodePos = detail_points[node]
                nodeX, nodeY = nodePos
                nextX1, nextX2, nextY1, nextY2 = next_node
                # next box formula from piazza
                nextPos = (min(nextX2-1,max(nextX1,nodeX)), min(nextY2-1,max(nextY1,nodeY)))
                detail_points[next_node] = nextPos
                if curr_goal == 'destination':
                    tentative = forward_dist[node] + eucDist(detail_points[node], detail_points[next_node])
                else:
                    tentative = backward_dist[node] + eucDist(detail_points[node], detail_points[next_node])
                if curr_goal == 'destination':
                    if next_node not in forward_dist or tentative < forward_dist[next_node]:
                        visited_nodes.append(next_node)
                        forward_dist[next_node] = tentative
                        forward_prev[next_node] = node
                        heappush(queue, (tentative + eucDist(detail_points[next_node], destination_point), next_node, 'destination'))
                else:
                    if next_node not in backward_dist or tentative < backward_dist[next_node]:
                        visited_nodes.append(next_node)
                        backward_dist[next_node] = tentative
                        backward_prev[next_node] = node
                        heappush(queue, (tentative + eucDist(detail_points[next_node], source_point), next_node, 'source'))

        if node in backward_prev and node in forward_prev:
            path = []
            detail_points[src] = source_point
            detail_points[dst] = destination_point
            
            nodeCopy = node
            while node:
                prevNode = forward_prev[node]
                if prevNode is not None:
                    path.append((detail_points[node], detail_points[prevNode]))
                node = prevNode
            while nodeCopy:
                prevNode = backward_prev[nodeCopy]
                if prevNode is not None:
                    path.append((detail_points[nodeCopy], detail_points[prevNode]))
                nodeCopy = prevNode
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