from copy import deepcopy as copy

# some matrices to play with
filled_four_x_four = [[1, 2, 3, 4], ["C", "D", "E", 5], ["B", "G", "F", 6], ["A", 9, 8, 7]]
filled_two_x_two = [[0, 1], [3, 2]]


# use this dict as an easy way to flip through sides
next_side = {"top":"right", "right":"bottom", "bottom":"left", "left":"top"}


def print_matrix(m):
	""" pretty prints a rectangular 2d matrix """
	for row in m:
		line = ""
		for elt in row: line += (str(elt) + " ")
		print line
	return


def trim(m, side):
	""" returns a copy of m with the specified side removed """
	if side == "top": return m[1:]
	if side == "bottom": return m[:len(m)-1]
	out = []
	for row in m:
		out.append(row[:len(row)-1] if side == "right" else row[1:])
	return out


def trimmed(m, side):
	""" returns the side that's removed by trim """
	if side == "top": return m[0]
	if side == "bottom": return m[len(m)-1]
	out = []
	for row in m:
		out.append(row[len(row)-1] if side == "right" else row[0])
	return out


def split(m, side):
	""" returns a tuple containing the removed side and the matrix with side removed """
	if side == "top": return (m[0], m[1:])
	if side == "bottom": return (m[len(m)-1], m[:len(m)-1])
	removed_side = []
	trimmed_matrix = []
	for row in m:
		removed_side.append(row[len(row)-1] if side == "right" else row[0])
		trimmed_matrix.append(row[:len(row)-1] if side == "right" else row[1:])
	return (removed_side, trimmed_matrix)


def spiral(m, side="top"):
	if m == [[]] or m == []: return []

	traversed_side = []
	if side == "top" or side == "right": traversed_side = copy(split(m, side)[0])
	if side == "bottom" or side == "left": traversed_side = list(reversed(split(m, side)[0]))
	print "traversing " + side + " side, " + str(traversed_side) + ", of matrix"
	print_matrix(m)
	return traversed_side + spiral(split(m, side)[1], next_side[side])


print spiral(filled_four_x_four)