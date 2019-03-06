#Quick Sort

def QuickSort(num_list):
	if len(num_list) <= 1:
		return num_list

	left = []
	right = []
	base = num_list.pop()
	for number in num_list:
		if number <= base:
			left.append(number)
		else:
			right.append(number)

	return QuickSort(left) + [base] + QuickSort(right)

if __name__ == '__main__':
	num_list = [1, 1, 13, 55, 34, 8, 23, 89]
	res = QuickSort(num_list)
	print(res)
