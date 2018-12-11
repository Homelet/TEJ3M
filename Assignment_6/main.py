from collections.abc import Iterable


def fetch_unique(li):
	if li is None:
		assert False, "Can't Fetch from NoneType"
	if not isinstance(li, Iterable):
		assert False, "Item not Iterable"
	buffer = []
	merge_sort(data=li)
	for i in li:
		if i not in buffer:
			buffer.append(i)
	return buffer


def merge_sort(data):
	split(data, 0, data.__len__() - 1)


def split(data, left_bounds, right_bounds):
	# if left bounds is equals or bigger than right bounds means the left and right collapsed
	if left_bounds >= right_bounds:
		return
	
	# calculate the middle
	middle = (left_bounds + right_bounds) // 2
	# continue to split the to left part and right part
	split(data, left_bounds, middle)
	split(data, middle + 1, right_bounds)
	# if spitted, starts merging
	merge(data, left_bounds, middle, right_bounds)


def merge(data, left_bounds, mid, right_bounds):
	sub_data = data[left_bounds: right_bounds + 1]
	# init, left_pointer points to left start, right_pointer points right start
	left_pointer = left_bounds
	right_pointer = mid + 1
	# iterate through the whole collection
	index = left_bounds
	while index <= right_bounds:
		if left_pointer > mid:
			# if all left has been processed
			data[index] = sub_data[right_pointer - left_bounds]
			right_pointer += 1
		elif right_pointer > right_bounds:
			# if all right has been processed
			data[index] = sub_data[left_pointer - left_bounds]
			left_pointer += 1
		elif compare_to(sub_data[left_pointer - left_bounds], sub_data[right_pointer - left_bounds]) < 0:
			# if left data < right data then let left data add
			data[index] = sub_data[left_pointer - left_bounds]
			left_pointer += 1
		else:
			# if left data >= right data then let right data add
			data[index] = sub_data[right_pointer - left_bounds]
			right_pointer += 1
		index += 1


def compare_to(data_1, data_2):
	if type(data_1) is not type(data_2):
		assert False, "Can not compare two value with different type"
	if data_1 > data_2:
		return 1
	elif data_1 < data_2:
		return -1
	else:
		return 0


if __name__ == '__main__':
	test_case_1 = [7, 5, 10, 23123, 131123, 124, 1234, 6, 7, 5, 10]  # pass
	test_case_2 = [1, 2, 3, 4, 5, 6, 7]  # pass
	test_case_3 = []  # pass
	test_case_4 = [1, '234567']  # fail because NaN
	test_case_5 = 1  # fail because non-iterable
	test_case_6 = None  # fail because None
	print(fetch_unique(test_case_6))
	print(test_case_6)
