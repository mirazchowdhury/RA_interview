def sort_val(nums):
	count = [0,0,0]
	for num in nums:
		count[num] += 1
		
	sorted_nums =  [0]*count[0] + [1]*count[1] + [2]*count[2]
	return sorted_nums

print(sort_val([2,0,2,1,1,0])) 