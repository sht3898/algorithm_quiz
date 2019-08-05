def jarisu(number):
    number = int(number)
    result = 0
    while number > 0:
        result += number % 10
        number = number // 10
    return print(result)

jarisu(6789)