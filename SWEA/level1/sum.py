def my_sum(testcase):
    result = 0
    for i in range(testcase):
        result += i + 1
    return str(result)

a = int(input())
print(my_sum(a))