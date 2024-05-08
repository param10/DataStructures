def merge(left, right):
    merged =  []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    while i < len(left):
            merged.append(left[i])
            i += 1
    while j < len(right):
            merged.append(right[j])
            j += 1
    return merged



def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    index = int(len(my_list)/2)
    left = merge_sort(my_list[:index])
    right = merge_sort(my_list[index:])

    return merge(left, right)



original_list = [3,1,4,2]

sorted_list = merge_sort(original_list)

print('Original List:', original_list)

print('\nSorted List:', sorted_list)
