import csv

#  Creating a function to use it in Task7 and in the Task6_modified_for_Task7
def count_letters(input_filename, output_filename):

    # Read input file, i.e. output.txt
    input_file = open(input_filename, "r")
    input = input_file.read()
    input_file.close()

    # Calculate total number of symbols excluding special
    exclude_symbols = (' ', '\t', '\n')
    letters_number = len(input)
    for ex_symbol in exclude_symbols:
        letters_number -= input.count(ex_symbol)

    # Create the list of normalized words: lowercase, remove punctuation marks
    letters = {}
    for i in range(len(input)):
        letter = input[i].lower()
        if letter not in exclude_symbols and letter not in letters.keys():
            new_letter = {}
            upper = input.count(letter.upper())
            lower = input.count(letter.lower())

            # Add dictionary entry
            new_letter['letter'] = letter
            new_letter['count_all'] = upper + lower
            new_letter['count_uppercase'] = upper
            new_letter['percentage'] = round((upper + lower)/letters_number * 100, 2)
            letters[letter] = new_letter

    # Create CSV file with header
    with open(output_filename, 'w', newline='') as output_file:
        header = ['letter', 'count_all', 'count_uppercase', 'percentage']
        output = csv.DictWriter(output_file, fieldnames=header, delimiter='-')
        output.writeheader()
        for letter in letters.keys():
            output.writerow(letters[letter])
        output_file.close()
