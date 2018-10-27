#Binary Search

def binary_search(num_list, target):
	i = 0
	j = len(num_list) - 1
	if num_list[0] < num_list[j]:
		order = True
	else:
		order = False
	count = 0
	while i <= j:
		count += 1
		m = (i + j) // 2
		if target == num_list[m]:
			return m
		if num_list[m] < target:
			if order == True:
				i = m + 1
			else:
				j = m - 1
		else:
			if order == True:
				j = m - 1
			else:
				i = m + 1
	return -1

if __name__ == '__main__':
	numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
	n = int(input())
	print(binary_search(numbers, n))