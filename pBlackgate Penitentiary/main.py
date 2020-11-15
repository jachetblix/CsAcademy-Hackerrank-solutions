num = int(input())
jokers_streetGang = {}
heights = []
lines_count = 1
for i in range(num):
    name, position = input().split()
    position = int(position)
    if position not in jokers_streetGang:
        jokers_streetGang[position] = (name)
    else:
        jokers_streetGang[position] += (' ' + name)

    if position not in heights:
        heights.append(position)

heights.sort()
for h in heights:
    names = jokers_streetGang[h].split()
    names.sort()
    print(' '.join(names) + ' ' + str(lines_count) + ' ' + str(lines_count + len(names) - 1))
    lines_count = lines_count + len(names)