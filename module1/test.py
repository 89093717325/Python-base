def sort_list(my_list, direction=None):
    
    # Если direction не указан, то просто возвращаем параметр my_list
    if direction is None:
        return my_list

    for i in range(len(my_list)):
        for j in range(i, len(my_list)):            
            if (direction == 1 and my_list[i] > my_list[j]) or (direction != 1 and my_list[i] < my_list[j]):
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp

    return my_list

list1 = [4, -2, 5, 3, -1 , 1, 0, 5, 2]
list2 = [5, 3, 2, 5, 6 , -1, 0, -5, 2]
list3 = [7, 2, 4, 1, -1 , 7, 3, -5, 0]
list4 = [2, -5, 6, 1, 0 , -1, -2, -3, 9]
list5 = [9, 0, 1, 2, 9 , 3, -1, 4, 2]

sort_list(list1, 1)
sort_list(list2)
sort_list(list3, 1)
sort_list(list4)
sort_list(list5, 0)

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
