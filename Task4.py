# ///////////Refactored Task #3/////////////
def split_paragraph(_paragraph):                    # Creation of the function which splits paragraph into the sentences
    _sentences = []
    _sentences = _paragraph.split(".")              # Splitting paragraph into a sentences using dot as a separator
    _sentences.remove('')                           # Removing empty strings if any
    for _i in range(0, len(_sentences)):
        _sentences[_i] = _sentences[_i].lstrip()    # Remove spaces to the left
        _sentences[_i] += '.'                       # Adding a dot at the end of sentence
    return _sentences

def normalize_sentence(_sentence):                  # Creating of the function which normalize sentences
    _sentence = _sentence.strip()                   # Removing spaces at the beginning and at the end of the sentenses
    _sentence = _sentence.lower()                   # Lower case for the letters in paragraph
    _sentence = _sentence.capitalize()              # Changing first character of the sentence to upper case
    return _sentence

def join_paragraphs(_paragraphs):                   # Creating function to join paragraphs into multiline
    _joined_paragraph = ""                          # Create a variable for multiline output
    for i in range(0, len(_paragraphs) - 1):        # Join all but last strings with line break
        _joined_paragraph += _paragraphs[i] + "\n"
    _joined_paragraph += _paragraphs[-1]            # Add the last string without line break
    return _joined_paragraph                        # Return multiline string

# Define source paragraphs
str = """"""
paragraphs = str.split("\n")

# Normalize paragraphs
norm_paragraphs = []                                            # Adding new variable
for paragraph in paragraphs:
    sentences = split_paragraph(paragraph)                      # Split paragraph to sentences
    norm_paragraph = ""                                         # Adding new variable norm_paragraph
    for sentence in sentences:
        norm_paragraph += normalize_sentence(sentence) + " "    # Adding sentences to the norm_paragraph
    norm_paragraphs.append(norm_paragraph.rstrip(" "))          # Adding sentences to norm_paragraphs
print("\nNORMALIZED PARAGRAPHS")
print(join_paragraphs(norm_paragraphs))


# Create additional sentence, I split norm_paragraphs into sentences, sentence into words and find the last word of each sentence
additional_sentance = ""                                        # Adding new string variable
for paragraph in norm_paragraphs:
    sentences = split_paragraph(paragraph)                      # Splitting paragraph using dot
    for sentence in sentences:
        words = sentence.split(" ")                             # Splitting sentence to words
        additional_sentance += words[-1].rstrip('.') + " "      # Adding the last word of the sentence without dot to additional_sentance
additional_sentance = additional_sentance.rstrip(" ") + "."     # Trip trailing space and add dot at the end of the sentence
norm_paragraphs.append(additional_sentance.capitalize())        # Adding capitalized additional sentence to the norm_paragraphs
print("\nCREATED SENTENCE FROM THE LAST WORDS:")
print(norm_paragraphs[-1])


# Calculate spaces
print("\nTHE NUMBER OF SPACES ARE:", str.count(" "))


# Changing 'iz' to 'is' in the right places:
for i in range(0, len(norm_paragraphs)):
    norm_paragraphs[i] = norm_paragraphs[i].replace(" iz ", " is ")    # Replacing 'iz' with 'is'
print("\nWITH CORRECT 'IS' INSTEAD OF 'IZ':")
print(norm_paragraphs)
print(join_paragraphs(norm_paragraphs))

