def remove_duplicates(list1):
    list2 = []

    if list1:
        for item in list1:
            if item not in list2: # is item in list2 already?
                list2.append(item)
    else:
        return list1
    return list2

print(remove_duplicates([1,2,3,3,4,5]))