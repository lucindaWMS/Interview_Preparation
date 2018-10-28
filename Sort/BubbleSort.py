#Bubble Sort

def BubbleSort(num_list):
	for i in range(len(num_list) - 1):
		for j in range(len(num_list) - i - 1):
			if num_list[j] > num_list[j+1]:
				temp = num_list[j]
				num_list[j] = num_list[j+1]
				num_list[j+1] = temp
	return num_list

if __name__ == '__main__':
	num_list = [1, 1, 13, 55, 34, 8, 23, 89]
	res = BubbleSort(num_list)
	print(res)
