"""
найти сумму цифр, из которых состоит строка.
"""
import sys


digit_str = sys.argv[0]
print(digit_str)


while True:
    input_str = input()
    if not input_str.isdigit():
        print('В строке должны быть только числа')
    else:
        sum_num = 0
        for num in input_str:
            sum_num += int(num)
        print(sum_num)
        break



