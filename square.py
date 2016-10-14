start_list = [5,3,1,2,4]
square_list = []
for x in start_list:
    square_list_temp = x**2
    square_list.append(square_list_temp)
square_list.sort()
print (square_list)
