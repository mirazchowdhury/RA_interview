def merge_sorted_arrays(num1,num2):
    i = j = 0
    merged_array = []
    
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            merged_array.append(num1[i])
            i += 1
        else:
            merged_array.append(num2[j])
            j += 1
            
    merged_array.extend(num1[i:])
    merged_array.extend(num2[j:])
    return merged_array

nums1 = [1,3,5]
nums2 = [2,4,6]
merged_array = merge_sorted_arrays(nums1, nums2)    
print(merged_array)