def insomnia(number):
    num_list = []
    num = number
    while len(num_list) < 10:
        num = str(num)
        for idx in num:
            if idx not in num_list:
                num_list.append(idx)
        num = int(num)
        num += number
    return int(num) - int(number)

b = int(input())

for i in range(b):
    a = int(input())
    print(f'#{i+1} {insomnia(a)}')
