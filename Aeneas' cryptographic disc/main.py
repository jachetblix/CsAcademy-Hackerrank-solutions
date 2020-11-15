# author Artem Egorov
import math as m

number_of_input_points = float(input())
my_dict = {}
for i in range(26):
    letter, letter_distance = input().split()
    my_dict[letter] = float(letter_distance)
lent = 0
phrase_paragraph = input().replace(" ", "").upper()
only_alpha = ""
for char in phrase_paragraph:
    if 65 <= ord(char) <= 90:
        only_alpha += char
temp_arr = my_dict[only_alpha[0]]
for i in only_alpha[1:]:
    x = my_dict[i]
    x = float(x)
    difference = 2 * number_of_input_points * abs(m.sin(m.radians((x - temp_arr) / 2)))
    temp_arr = x
    lent = lent + difference
print(m.ceil(lent + number_of_input_points))
