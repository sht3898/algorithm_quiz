
test = [[3, 8], [7, 7], [369, 123]]
result = [] * len(test)

for idx in range(len(test)):
    if test[idx][0] < test[idx][1]:
        result.append('<')
    elif test[idx][0] == test[idx][1]:
        result.append('=')
    else:
        result.append('>')
    print(f'#{idx+1} {result[idx]}')