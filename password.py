# Davis Arita
# 10/12/2022
# CS 131 Exercise 7 Part C
# program prompts for password twice and checks them for match and checks if
# password matches criteria

def main():

    done = False
    while not done:
        password = input("Enter your password: ")
        if password_compare(password):
            if password_valid(password):
                print("That pair of passwords will work.")
                done = True
            else:
                print("That password didn't have the required properties.")
        else:
            print("That passwords don't match")


def password_compare(password):
    pass_compare = input("Re-Enter your password: ")
    same = True
    for index in range(len(password)):
        if password[index] != pass_compare[index]:
            same = False

    return same


def password_valid(password):
    special_characters = "#@&"
    if len(password) >= 8:
        for i in range(len(password)):
            digit_count = 0
            special_count = 0
            if password[i].isupper():
                upper_case = True
            if password[i].islower():
                lower_case = True
            if password[i].isdigit():
                digit_count += 1
        if any(c in '#@&' for c in password):
            special_count += 1
        if (digit_count >= 1) and (special_count >= 1) and upper_case and lower_case:
            return True
        else:
            return False
    else:
        return False


main()
