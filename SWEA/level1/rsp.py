def rsp(a, b):
    # 1: 가위
    # 2: 바위
    # 3: 보
    if a == 1 and b == 2:
        print('B')
    elif a == 2 and b == 3:
        print('B')
    elif a == 3 and b == 1:
        print('B')
    elif a == 1 and b == 3:
        print('A')
    elif a == 2 and b == 1:
        print('A')
    elif a == 3 and b == 2:
        print('A')
    else:
        return False


x, y = map(int, input().split())
rsp(x, y)