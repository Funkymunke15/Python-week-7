# Davis Arita
# 10.12.22
# CS 131 Exercise 7 part A
# if a word is 4 or more characters long, swap the second character and the
# second to last character

## Scrambles the second and second to last characters in a word in a string
# @param string to have words scrambled
#
def scramble(string):
    temp_string = ""
    for word in string.split(" "):
        temp_word = ""
        if len(word) >= 5:
            temp_word = word[0] + word[-2]
            temp_word += word[2:-2]
            temp_word += word[1]
            temp_word += word[-1]
            temp_string = temp_string + temp_word + " "
        elif len(word) == 4:
            temp_word = word[0] + word[-2] + word[1] + word[-1]
            temp_string = temp_string + temp_word + " "
        else:
            temp_string = temp_string + word + " "

    return temp_string


def main():
    string = input("Enter a string (blank to quit): ")
    done = False
    
    while not done:
        if len(string) == 0:
            done = True
        else:
            print("THe scrambled version:", scramble(string))
            string = input("Enter a string (blank to quit): ")


main()
