def calculate_weight(x_data, y_data):
	n = x_data.__len__()
	m = (
			((n * sum_all(x_data, y_data, 0, n - 1, lambda x, y: x * y)) - (
				sum_all(x_data, y_data, 0, n - 1, lambda x, y: x)) * (
				 sum_all(x_data, y_data, 0, n - 1, lambda x, y: y))) /
			((n * sum_all(x_data, y_data, 0, n - 1, lambda x, y: x ** 2)) - (
				sum_all(x_data, y_data, 0, n - 1, lambda x, y: x)) ** 2)
	)
	return m


def calculate_bias(x_data, y_data):
	pass


def sum_all(x_data, y_data, a, b, func):
	i = a
	sum_res = 0
	while i < b:
		sum_res += func(x_data[i], y_data[i])
		i += 1
	return sum_res


def convert_to_float(s):
	try:
		return float(s)
	except ValueError:
		assert False, "\"" + s + "\" can't be converted"


def readFile(file_name):
	ls = []
	with open(file_name, "r") as f:
		while True:
			s = f.readline()
			if s == '':
				break
			ls.append(convert_to_float(s.replace('\n', '')))
	return ls


if __name__ == '__main__':
	file_prefix = input("File prefix : ")
	x_file_name = file_prefix + "_x"
	y_file_name = file_prefix + "_y"
	x_data = readFile(x_file_name)
	y_data = readFile(y_file_name)
	assert x_data.__len__() == y_data.__len__(), "Data does not has a same length"
	assert x_data.__len__() is not 0, "No data acquired"
	print("Appropriate description=" + str(calculate_weight(x_data, y_data)))
