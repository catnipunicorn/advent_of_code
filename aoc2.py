with open('day2.txt', 'r') as file:
	data = file.readlines()
	direction = []
	for i in data:
		if 'forward' in i:
			f = i
			for m in f.split():
				if m.isnumeric():
					direction.append(int(m))

	total_dir = (sum(direction))
	depth = []
	for x in data:
		if 'down' in x:
			y = x
			for z in x.split():
				if z.isnumeric():
					depth.append(int(z))
	total_depth = (sum(depth))
	up = []
	for d in data:
		if 'up' in d:
			e = d
			for a in e.split():
				if a.isnumeric():
					up.append(int(a))
	total_up = (sum(up))
	answer = total_dir * (total_depth - total_up)
	print(answer)