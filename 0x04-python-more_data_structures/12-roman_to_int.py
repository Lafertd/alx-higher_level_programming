#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return(0)

    rom_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in roman_string:
        if i not in rom_dic.keys():
            return(0)
    num = 0

    for i in range(len(roman_string)):
        if (i != (len(roman_string) - 1) and
                rom_dic[roman_string[i]] < rom_dic[roman_string[i + 1]]):
                num += rom_dic[roman_string[i]] * -1

        else:
            num += rom_dic[roman_string[i]]

    return(num)
