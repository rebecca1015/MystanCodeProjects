"""
File: largest_digit.py
Name: Rebecca
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	return find_largest_digit_helper(n, 0)


def find_largest_digit_helper(n, largest_num):
	"""
	:param n: integer
	:param largest_num: first data
	:return largest_num: the biggest digit in integer
	"""
	n = abs(n)
	a = n % 10
	if n / 10 == 0 and n % 10 == 0:
		return largest_num
	else:
		if a > largest_num:
			largest_num = a
		return find_largest_digit_helper(n//10, largest_num)


if __name__ == '__main__':
	main()
