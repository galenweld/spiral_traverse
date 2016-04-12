from copy import copy as copy

four_x_four = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
filled_four_x_four = [[1, 2, 3, 4], ["C", "D", "E", 5], ["B", "G", "F", 6], ["A", 9, 8, 7]]
filled_two_x_two = [[0, 1], [3, 2]]


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
	if side == "top": return copy(m[0])
	if side == "bottom": return copy(m[len(m)-1])
	out = []
	for row in m:
		out.append(row[len(row)-1] if side == "right" else row[1])
	return out


def spiral_helper(m, side):
	print "matrix:"
	print_matrix(m)
	print ""
	if m == [[]] or m == []: return []

	side_contents = []
	if side == "top" or side == " right": side_contents = trimmed(m, side)
	if side == "bottom" or side == "left": side_contents = reversed(trimmed(m, side))
	return side_contents + spiral_helper(trim(m, side), next_side[side])


def spiral(m): return spiral_helper(m, "top")


print_matrix(spiral(filled_four_x_four))