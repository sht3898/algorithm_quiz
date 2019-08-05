a = int(input())

result = ''
for idx in range(1, a+1):
    if a % idx == 0:
        if idx == a:
            result += str(idx)
        else:
            result += str(idx)+' '
print(result)