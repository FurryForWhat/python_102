first_list = [1,2,7]
second_list = [1,2,3,4,5,6]

a = len(first_list)
b = len(second_list)
index_count = 0
if a > b:
    print('Program cannot working')

else:
    for i in range(a): # 3
        for j in range(b): # 6
            if second_list[j] == first_list[i]:
                index_count += 1
            else:
                pass
        
    if index_count == a:
        print('Yes')
    else:
        print('NO')