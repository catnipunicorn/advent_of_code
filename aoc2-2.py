with open('day2.txt', 'r') as file:
	data = file.readlines()
	horizontal = 0
	aim = 0
	depth = 0
	for i in data:
		if 'forward' in i:
			f = i
			for x in f.split():
				if x.isnumeric():
					move = int(x)
			horizontal = horizontal + move
			depth = depth + (aim * move)
		if 'down' in i:
			d = i
			for a in d.split():
				if a.isnumeric():
					sink = int(a)
			aim = aim + sink
		if 'up' in i:
			u = i
			for b in u.split():
				if b.isnumeric():
					fly = int(b)
			aim = aim - fly
	answer = horizontal * depth
	print(answer)