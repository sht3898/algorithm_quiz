def decomposition(number):
    result = [0, 0, 0, 0, 0]
    while number % 2 == 0:
        result[0] += 1
        number = number / 2
    while number % 3 == 0:
        result[1] += 1
        number = number / 3
    while number % 5 == 0:
        result[2] += 1
        number = number / 5
    while number % 7 == 0:
        result[3] += 1
        number = number / 7
    while number % 11 == 0:
        result[4] += 1
        number = number / 11
    for idx in range(len(result)):
        if idx == len(result) - 1:
            print(result[idx])
        else:
            print(result[idx], end=' ')

print('#1', end= ' '),decomposition(6791400)
print('#2', end= ' '),decomposition(1646400)
print('#3', end= ' '),decomposition(1425600)
print('#4', end= ' '),decomposition(8575)
print('#5', end= ' '),decomposition(185625)
print('#6', end= ' '),decomposition(6480)
print('#7', end= ' '),decomposition(1185408)
print('#8', end= ' '),decomposition(6561)
print('#9', end= ' '),decomposition(25)
print('#10', end= ' '),decomposition(330750)