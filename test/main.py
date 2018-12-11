# input_num = int(input("input a number :"))
#
# if input_num % 2 is 0:
# 	if input_num % 4 is 0:
# 		print("the number {} is dividable by 4".format(input_num))
# 	else:
# 		print("the number {} is even".format(input_num))
# else:
# 	print("the number {} is odd".format(input_num))
#
# # extra
# input_num = int(input("input a number : "))
# input_check = int(input("input a check : "))
#
# if input_num % input_check is 0:
# 	print("the number {} is dividable by {}".format(input_num, input_check))
# else:
# 	print("the number {} is not dividable by {}".format(input_num, input_check))

# ex2
a = [1, 2, 3, 4, 1, 2, 3, 1, 5, 1, 23, 56, 436, 4, 13, 346, 45746]

for i in a:
	if i < 5:
		print(i, end=", ")
print()

# extra 1
print([i for i in a if i < 5])

# extra 3
num = int(input("input a number : "))

print([i for i in a if i < num])
