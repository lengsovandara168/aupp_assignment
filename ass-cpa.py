# Application 1
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

# word = input('Enter the string: ')
# double_word = ''
# for char in word:
#     double_word += char*2
# print(double_word)

# Application 2
#  Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!

# Examples
# "a-z" ➞ "abcdefghijklmnopqrstuvwxyz"
# "h-o" ➞ "hijklmno"
# "Q-Z" ➞ "QRSTUVWXYZ"
# "J-J" ➞ "J"
# Notes A hyphen will separate the two letters in the string.

def generate_letter_range(user_range):
    start, end = user_range.split('-')
    start_index = ord(start)
    end_index = ord(end)

    result = ''.join(chr(i) for i in range(start_index, end_index + 1))

    return result.upper() if start.isupper() else result

user_range = input("Enter a range of letters (e.g., a-z): ")
result = generate_letter_range(user_range)
print(result)



# alphabet = "abcdefghijklmnopqrstuvwxyz"
# start, end = alphabet.split('-')
# user_range = input("Enter a range of letters (e.g., a-z): ")
# print(user_range)

