def calculation(number):
    if len(number) == int(number):
        print(int(number))
        return

    result = 0
    bool_iter = 0

    while result != len(number):
        result = len(number)
        number = str(result)
        bool_iter += 1
    bool_iter += 1
    print(bool_iter)


if __name__ == '__main__':
    number = input()
    while number != "END":
        calculation(number)
        number = input()