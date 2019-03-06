#Merge Sort
def MergeSort(num_list):
	if len(num_list) <= 1:
		return num_list

	mid = len(num_list) // 2
	left = MergeSort(num_list[:mid])
	right = MergeSort(num_list[mid:])
	return merge(left, right)

def merge(left, right):
	res = []
	while left and right:
		if left[0] < right[0]:
			res.append(left.pop(0))
		else:
			res.append(right.pop(0))
	res += left + right
	return res

if __name__ == '__main__':
	num_list = [1, 1, 13, 55, 34, 8, 23, 89]
	res = MergeSort(num_list)
	print(res)