student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    print(1)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
     print(index)
    #Access row.student or row.score


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

pd = pandas.read_csv("nato_phonetic_alphabet.csv")
code = pd["code"]
letter = pd["letter"]
keyword = {letter:code for letter, code in zip(letter,code)}
print(keyword)

user_input = input("Enter your name to decode.").upper()
output = [keyword[letter] for letter in user_input]
print(output)
