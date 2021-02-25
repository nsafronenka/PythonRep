import csv

#  Creating a function to use it in Task7 and in the Task6_modified_for_Task7
def count_words(input_filename, output_filename):

    # Read input file, i.e. output.txt
    input_file = open(input_filename, "r")
    input = input_file.read().split()
    input_file.close()

    # Create the list of normalized words: lowercase, remove punctuation marks
    words = []
    for word in input:
        if word[-1] in ('.', ',', '!', ':', '?'):
            words.append(word[:-1].lower())
        else:
            words.append(word.lower())

    # Create a dictiory of words number
    words_count = {}
    for word in words:
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1

    # Create CSV file with header
    with open(output_filename, 'w', newline='') as output_file:
        output = csv.writer(output_file, delimiter='-')
        output.writerow(['Word', 'Count'])
        for word in words_count.keys():
            output.writerow([word, words_count[word]])
        output_file.close()