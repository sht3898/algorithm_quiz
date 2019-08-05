for idx in range(5):
    for idx3 in range(idx):
        print('+',end='')
    print('#',end='')
    for idx2 in range(5-idx-1):
        print('+',end='')
    print('')