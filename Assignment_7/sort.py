import random
import time

from tabulate import tabulate


def bubble_sort(ls):
	"""
	the idea of bubble sort is that doing sort between the adjacent item
	and if a single round has no sort operations, it is finished
	
	:param ls: the list
	:return: the sorted list, the total swap, the total comparision
	"""
	# init the target buffer
	target = ls[:]
	# start a timer for testing the sort cost
	start_time = time.time()
	# accumulate the total swap, comparision
	total_swap, total_comparision = 0, 0
	# starting algorithm
	# get the length of the list, because it is frequently used
	length = target.__len__()
	# start a infinity loop, because we don't want it stop until it finnish sorting
	while True:
		# the swapped counter to count how many count swap has occur and reset the counter to 0
		swapped = 0
		# the cursor of the current iteration, it starts at 1 because it compares to the one to it before
		cursor = 1
		# the loop for the current iteration
		while cursor < length:
			# if the current cursor is smaller than the last one
			if target[cursor] < target[cursor - 1]:
				# accumulate the swap counter
				swapped += 1
				# perform the swap
				target[cursor - 1], target[cursor] = target[cursor], target[cursor - 1]
			# point to the next cursor
			cursor += 1
		# accumulate the comparision
		total_comparision += cursor
		# accumulate the swapped counter
		total_swap += swapped
		# if has no swap performed, then break
		if swapped == 0:
			break
	
	# return the result
	return target, total_swap, total_comparision, time.time() - start_time


def selection_sort(ls):
	"""
	the idea of selection sort is to find the minimum element in the following list and then swap it
	with the current cursor until all list sorted
	
	:param ls: the list
	:return: the sorted list, the total swap, the total comparision
	"""
	# init the target buffer
	target = ls[:]
	# start a timer for testing the sort cost
	start_time = time.time()
	# accumulate the total swap, comparision
	total_swap, total_comparision = 0, 0
	# get the length of the function because it is frequently used
	length = target.__len__()
	# the index that split the sorted and the unsorted
	cursor = 0
	# start a iteration through the list
	while cursor < length:
		# a indicator for the smallest in side the loop
		smallest = cursor
		# the inner_cursor is the cursor for the inner loop
		inner_cursor = cursor + 1
		# start the inner loop to iterate through the unsorted part
		while inner_cursor < length:
			# if the current pointing to is smallest to the smallest that is pointing to
			# then set the smallest to the inner_cursor
			if target[inner_cursor] <= target[smallest]:
				smallest = inner_cursor
			# increase the inner_cursor by 1
			inner_cursor += 1
		total_comparision += inner_cursor
		# swap the smallest number with the current cursor and the loop continues
		if cursor != smallest:
			# swap
			target[cursor], target[smallest] = target[smallest], target[cursor]
			# accumulate the swap
			total_swap += 1
		# increase the cursor by 1
		cursor += 1
	
	# return the result
	return target, total_swap, total_comparision, time.time() - start_time


def gen_random_list(length, low_bound=0, up_bound=100):
	"""
	generate a list of random number with low_bound <= s <= up_bound
    
	:param length: the length of the list
	:param low_bound: the low_bounds, default 0
	:param up_bound: the up_bounds, default 100
	:return: a list contains random numbers
	"""
	return [random.randint(low_bound, up_bound) for _ in range(length)]


def test_successful(ls):
	"""
	test whether the list is in a ascendent order
	
	:param ls: the list
	:return: a bool indicate it is success or not
	"""
	prev = ls[0]
	index = 1
	while index < ls.__len__():
		if ls[index] < prev:
			return False
		index += 1
	return True


TEST_BASE = [5, 10, 50, 100, 500, 1000]


def test_sort(sort_method, test_data=None):
	"""
	test a single sort algorithm, and print the test result, the result include the
	size of the buffer, and the total comparisons, and the it is successful or not,
	and the time cost
	
	:param sort_method: the method perform the sort
	:param test_data: the test data, if not specific then will generate one
	:return: the test_data
	"""
	# if the test_data is not given then generate one
	if test_data is None:
		test_data = [gen_random_list(i) for i in TEST_BASE]
	test_result = []
	# start the test
	for test in test_data:
		# grab the data from the algorithm
		sorted_test, total_swap, total_comparision, time_cost = sort_method(test)
		test_result.append([test.__len__(), total_swap, total_comparision, test_successful(sorted_test), time_cost])
	print(tabulate(test_result, headers=("Size", "# of Swaps", "# of comparisons", "Success", "Time Cost")))
	# return the test data
	return test_data


def test_both_sort(sort_method_1, sort_method_2, test_data=None):
	"""
	test a two sort algorithm, and print the test result to compare them, the result include the
	size of the buffer, and the total comparisons, and the it is successful or not,
	and the time cost
	
	:param sort_method_1: the method 1 perform the sort
	:param sort_method_2: the method 2 perform the sort
	:param test_data: the test data, if not specific then will generate one
	:return: the test_data
	"""
	# if the test_data is not given then generate one
	if test_data is None:
		test_data = [gen_random_list(i) for i in TEST_BASE]
	test_result = []
	# start the test
	for test in test_data:
		# grab the data from the first algorithm
		sorted_test_1, total_swap_1, total_comparision_1, time_cost_1 = sort_method_1(test)
		# grab the data from the second algorithm
		sorted_test_2, total_swap_2, total_comparision_2, time_cost_2 = sort_method_2(test)
		
		test_result.append(
				[test.__len__(), total_swap_1, total_comparision_1, test_successful(sorted_test_1), time_cost_1])
		test_result.append(
				[None, total_swap_2, total_comparision_2, test_successful(sorted_test_2), time_cost_2])
	print(tabulate(test_result, headers=("Size", "# of Swaps", "# of comparisons", "Success", "Time Cost")))
	# return the test data
	return test_data


if __name__ == "__main__":
	test_both_sort(bubble_sort, selection_sort)
