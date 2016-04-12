from copy import deepcopy as copy

verbose = True

# some matrices to play with
four_x_four = [[1, 2, 3, 4], ["C", "D", "E", 5], ["B", "G", "F", 6], ["A", 9, 8, 7]]
two_x_two = [[0, 1], [3, 2]]
small_rect = [[0, 1, 2, 3, 4, 5], ["D", "E", "F", "G", "H", 6], ["C", "B", "A", 9, 8, 7]]
large_rect = [[0, 1, 2, 3, 4, 5, 6, 7], ["J", "K", "L", "M", "N", "O", "P", 8],
				["I", "V", "U", "T", "S", "R", "Q", 9], ["H", "G", "F", "E", "D", "C", "B", "A"]]


# use this dict as an easy way to flip through sides
next_side = {"top":"right", "right":"bottom", "bottom":"left", "left":"top"}


def print_matrix(m):
	""" pretty prints a rectangular 2d matrix """
	for row in m:
		line = ""
		for elt in row: line += (str(elt) + " ")
		print line
	return


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
	if verbose:
		print "traversing " + side + " side, " + str(traversed_side) + ", of matrix"
		print_matrix(m)
	return traversed_side + spiral(split(m, side)[1], next_side[side])


print spiral(large_rect)