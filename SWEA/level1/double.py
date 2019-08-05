def double(number):
    for idx in range(number + 1):
        if idx != number + 1:
            print(2 ** idx, end=' ')
        else:
            print(2 ** idx)

a = int(input())
double(a)