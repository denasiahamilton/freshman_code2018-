n = 10

def multTable (n):
		table = []
		for i in range(n):
			row = [ ]
			for j in range(n):
				row.append((j+1) * (i+1))
			table.append(row)
		return table
print (multTable(n))
