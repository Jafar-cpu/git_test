def largest_two(a):
    my_max = a[0]
    my_max2 = a[1]
    if my_max < my_max2:
        my_max,my_max2 = my_max2,my_max
        
    for i in range(1,len(a)):
        if my_max < a[i]:
            my_max,my_max2 = a[i],my_max
        elif my_max2 < a[i]:
            my_max2 = a[i]
        
    return my_max,my_max2
        

a = [9,6,7,8,4,5,3,2,1]
print(None * 12)