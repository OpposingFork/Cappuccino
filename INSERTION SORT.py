arr = [2, 6, 5, 1, 3, 4]
def insertion_sort(are):
	for i in range(1, len(arr)):
	 j = i
	 while arr[j -1] > arr[j] and j > 0:
	 	arr[j - 1], arr[j] = arr[j], arr[j - 1]
	 	j -=1

insertion_sort(arr)
print(arr)