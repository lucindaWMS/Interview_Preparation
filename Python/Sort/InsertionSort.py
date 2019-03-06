#Insertion Sort

def InsertionSort(num_list):
	for i in range(1, len(num_list) - 1):
		j = i
		while j > 0 and num_list[j] < num_list[j-1]:
			num_list[j-1], num_list[j] = num_list[j], num_list[j-1]
			j -= 1
	return num_list

if __name__ == '__main__':
	num_list = [1, 1, 13, 55, 34, 8, 23, 89]
	res = InsertionSort(num_list)
	print(res)
