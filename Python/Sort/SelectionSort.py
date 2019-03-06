#Selection Sort

def SelectionSort(num_list):
	for i in range(len(num_list)):
		min_index = i
		for j in range(i+1, len(num_list)):
			if num_list[j] < num_list[min_index]:
				min_index = j
		num_list[min_index], num_list[i] = num_list[i], num_list[min_index]
	return num_list

if __name__ == '__main__':
	num_list = [1, 1, 13, 55, 34, 8, 23, 89]
	res = SelectionSort(num_list)
	print(res)