# Davis Arita
# 10.12.2022
# CS 131 Lecture 7B Lab 1
# calculates the sum of numbers 0 to n, where n is entered by user


def find_sum(param_num):
    sum_of_num = 0
    for i in range(param_num+1):
        sum_of_num += i
    return sum_of_num


num = int(input("Enter an integer: "))

print("The result is", find_sum(num))

