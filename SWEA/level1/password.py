def password(number, start):
    if number - start > 0:
        return number - start + 1
    else:
        return 999 - (number - start)

print(password(123, 100))