def zigzag(number):
    odd_list = []
    even_list = []
    result = 0
    for idx in range(1, number+1):
        if idx % 2:
            odd_list.append(idx)
        else:
            even_list.append(idx)

    for odd in odd_list:
        result += odd
    for even in even_list:
        result -= even
    

    return result

a = int(input())
for i in a:
    