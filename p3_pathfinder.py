def find_path(source_point, destination_point, mesh):
	path = []
	visited_nodes = []
	queue = []
	detail_points = {}
	start_box = box_from_point(source_point, mesh)
	end_box = box_from_point(destination_point, mesh)
	"""path.append((source_point, destination_point))"""
	queue.append(start_box)
	visited_nodes.append(start_box)
	temp = source_point
	detail_points[start_box] = temp
	while queue != []:
		box = queue[0]
		del queue[0]
		if box == end_box:
			break
		if box == None:
			print "No path!"
			return [], []
		for boxes in mesh['adj'][box]:
			visited_nodes.append(boxes)
			queue.append(boxes)
			pathBoxes = pathPoint(boxes, temp)
			detail_points[boxes] = pathBoxes
			print temp
			print pathBoxes
			temp = pathBoxes

	temp = source_point
	first = True
	for box, point in detail_points.iteritems():
		if first == True:
			path.append((temp, point))
			temp = point
			first = False
		else:
			path.append((temp, point))
			temp = point
	path.append((temp,destination_point))

	return path, visited_nodes


	

def box_from_point(point, mesh):
	x, y = point
	for box in mesh['boxes']:
		x1, x2, y1, y2 = box
		if(x >= x1 and x <= x2 and y >= y1 and y <= y2):
			return box

	return None

def pathPoint(box, currPoint):
	x1, x2, y1, y2 = box
	currX , currY = currPoint
	y = min(y1 - 1, max(x1,currY))
	x = min(x2 - 1, max(x1,currX))
	return (x,y)