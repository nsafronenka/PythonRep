import os
from Task6_1_module import Tip, News, PrivateAd
from Task6_2_module import Paragraph

# CALL FUNCTIONS FOR TASK 7
from Task7_1 import count_words
from Task7_2 import count_letters


# Ask for an input file path
input_filename = ""
input_filename = input("Input path to a source file or press Enter to use .\\input\\input.txt as default:\n")
if input_filename == "":
    input_filename = ".\\input\\input.txt"

# Read source content
input_file = open(input_filename, "r")
input_text = input_file.read()
input_file.close()

# Split content to paragraphs
paragraphs = input_text.split("\n")
content = []

# Parse content
str_num = 0
while str_num < len(paragraphs):
    current_str = paragraphs[str_num]
    if current_str[:5] == 'Type:':
        if current_str[6:] == 'Tip of the day':
            body = paragraphs[str_num + 1]
            body = Paragraph(body[6:]).normalized
            content.append(Tip(body))
            str_num += 2
        elif current_str[6:] == 'News':
            body = paragraphs[str_num + 1]
            body = Paragraph(body[6:]).normalized
            city = paragraphs[str_num + 2]
            content.append(News(body, city[6:]))
            str_num += 4
        elif current_str[6:] == 'Private Ad':
            body = paragraphs[str_num + 1]
            body = Paragraph(body[6:]).normalized
            expiration_time = paragraphs[str_num + 2]
            days_to_expire = paragraphs[str_num + 3]
            content.append(PrivateAd(body, expiration_time[17:]))
            str_num += 4
        else:
            print("Format error: Unknown or missing content type")
    str_num += 1

# Republish content
file = open("output.txt", "x")
file.write("NEWS FEED:\n\n")

for cur_content in content:
    cur_content.publish(file)
file.close()
# Commented for testing needs
# os.remove(input_filename)

#  THIS PART WAS ADDED FOR TASK 7
count_words("output.txt", "task7-1.csv")
count_letters("output.txt", "task7-2.csv")

