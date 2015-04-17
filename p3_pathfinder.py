def find_path(source_point, destination_point, mesh):
	path = []
	visited_nodes = []
	start_box = box_from_point(source_point, mesh)
	end_box = box_from_point(destination_point, mesh)
	path.append((source_point, destination_point))
	visited_nodes.append(start_box)
	visited_nodes.append(end_box)
	for box in mesh['adj'][start_box]:
		visited_nodes.append(box)
	for box in mesh['adj'][end_box]:
		visited_nodes.append(box)
	return path, visited_nodes

def box_from_point(point, mesh):
	x, y = point
	for box in mesh['boxes']:
		x1, x2, y1, y2 = box
		if(x >= x1 and x <= x2 and y >= y1 and y <= y2):
			print box
			return box

	return None