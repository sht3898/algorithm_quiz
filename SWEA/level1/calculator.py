def calculator(num1, num2):
    print(num1 + num2)
    print(abs(num1 - num2))
    print(num1 * num2)
    print(num1//num2)

a, b = map(int, input().split())
calculator(a, b)