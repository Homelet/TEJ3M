import re
import time


today = time.localtime(time.time())
pattern = "([012][0-9][0-9][0-9])[-/.]([01][0-9])[-/.]([0-3][0-9])"
day_dic = {
	1:  31,
	3:  31,
	4:  30,
	5:  31,
	6:  30,
	7:  31,
	8:  31,
	9:  30,
	10: 31,
	11: 30,
	12: 31,
}


# check if the birthday is validate
def check_validate(year, month, day):
	# if has a incorrect month
	if month > 12 or month < 1:
		print("incorrect month")
		return -1
	# if the month has a incorrect day
	if day < 0:
		print("incorrect day - negative")
		return -1
	if month == 2:
		if (year % 4 == 0 and year % 100 != 9) or (year % 400 == 0):
			if day > 29:
				print("incorrect day - overflow")
				return -1
		else:
			if day > 28:
				print("incorrect day - overflow")
				return -1
	else:
		if day > day_dic[month]:
			print("incorrect day - overflow")
			return -1
	# if has a incorrect year
	if year > today.tm_year:
		print("incorrect year - date after today")
		return -1
	elif year == today.tm_year:
		if check_md_before_today(month, day):
			return today.tm_year - year
		else:
			print("incorrect year - date after today")
			return -1
	return today.tm_year - year + (0 if check_md_before_today(month, day) else -1)


def check_md_before_today(month, day):
	# check if month correct
	if month > today.tm_mon:
		return False
	elif month == today.tm_mon:
		# check if day correct
		if day >= today.tm_mday:
			return False
		else:
			return True
	else:
		return True


if __name__ == "__main__":
	name = input("what is your name?")
	age = 0
	year = 0
	month = 0
	day = 0
	while True:
		birthday_str = input("what is your birthday(yyyy/mm/dd)?")
		if birthday_str == "quit":
			break
		matcher = re.search(pattern=pattern, string=birthday_str)
		if matcher is None:
			print("incorrect format")
			continue
		birthday_buff = matcher.groups()
		if birthday_buff.__len__() is not 3:
			print("incorrect format")
			continue
		s_year, s_month, s_day = birthday_buff
		year, month, day = int(s_year), int(s_month), int(s_day)
		result = check_validate(year, month, day)
		if result is -1:
			continue
		else:
			age = result
			break
	year_after_100 = year + 100
	print("\"%s\", %d years old, the date you will reach 100 years old is (%d/%d/%d)" %
		  (name, age, year_after_100, month, day))
