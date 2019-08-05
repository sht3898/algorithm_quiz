num_list = [[3, 17, 1, 39, 8, 41, 2, 32, 99, 2], 
        [22, 8, 5, 123, 7, 2, 63, 7, 3, 46],
        [6, 63, 2, 3, 58, 76, 21, 33, 8, 1]]

num_average = [0] * len(num_list)
for nums in range(len(num_list)):
    num_average[nums] = sum(num_list[nums])/len(num_list[nums])
    print(f'#{nums+1} {num_average[nums]:.0f}')