def size_suffix(temp_suffix, suffix_size, main_string):
    for j in main_string:
        if len(temp_suffix) == 0:
            break
        elif j == temp_suffix[0]:
            suffix_size +=1
            temp_suffix = temp_suffix[1:]
    return suffix_size


if __name__ == '__main__':
    string = input()
    string = string[::-1]
    query = int(input())
    for i in range(query):
        suffix = input()
        suffix = suffix[::-1]
        count = 0
        print(size_suffix(suffix, count, string))