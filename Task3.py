# Define source paragraphs
paragraphs = []
paragraphs.append("  tHis iz your homeWork, copy these Text to variable.")      # Adding sentences to paragraphs's list
paragraphs.append(
    "  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.")
paragraphs.append("  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.")
paragraphs.append(
    "  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces.")
paragraphs.append("I got 87.")
# Normalize paragraphs
norm_paragraphs = []                        # Adding new variable
for paragraph in paragraphs:                # Loop 'for' is used for iterating over a sequence in paragraphs
    paragraph = paragraph.lower()           # Lower case for the letters in paragraph
    paragraph = paragraph.strip()           # Removing spaces at the beginning and at the end of the sentences

    sentences = paragraph.split(".")        # Splitting paragraph into a sentences using dot as a separator
    sentences.remove('')                    # Removing spaces
    norm_paragraph = ""                     # Adding new variable norm_paragraph
    for sentence in sentences:
        sentence = sentence.lstrip(" ")     # Removing spaces to the left of the sentence
        sentence = sentence.capitalize()    # Changing first character of the sentence to upper case
        sentence += "."                     # Adding dot to the end of the sentence
        norm_paragraph += sentence + " "    # Adding sentences to the norm_paragraph
    norm_paragraph.rstrip(" ")              # Removing white spaces at the end
    norm_paragraphs.append(norm_paragraph)  # Adding sentences to norm_paragraphs
print(norm_paragraphs)
print()

# Create additional sentence, I split norm_paragraphs into sentences, sentence into words and find the last word of each sentence
additional_sentance = ""                    # Adding new string variable
for paragraph in norm_paragraphs:
    sentences = paragraph.split(".")        # Splitting paragraph using dot
    sentences.remove(' ')                   # Removing spaces
    for sentence in sentences:
        words = sentence.split(" ")         # Splitting sentence to words
        additional_sentance += words[len(words) - 1] + " "      # Adding the last word of the sentence to additional_sentance
additional_sentance = additional_sentance.rstrip(" ")           # Removing spaces at the end of the sentence between dot and the last word
additional_sentance += "."                                      # Adding dot at the end of the sentence
additional_sentance_capit = additional_sentance.capitalize()    # Changing first letter to capital
norm_paragraphs.append(additional_sentance_capit)               # Adding additional sentence to the norm_paragraphs
print()
print("CREATED SENTENCE FROM THE LAST WORDS: ", additional_sentance_capit)
print()
print("JOINED SENTENCE:\n")
for paragraph in norm_paragraphs:
    print(paragraph)
print()

# Calculate spaces
spaces = 0
for paragraph in norm_paragraphs:
    spaces += paragraph.count(" ")                          # Return number of whitespaces
print("THE NUMBER OF SPACES ARE: ", spaces)
print()

# Changing 'iz' to 'is' in the right places:
h = ""
for i in norm_paragraphs:
    h += i.replace(" iz ", " is ") + "\n"                    # Replacing 'iz' with 'is'
print("WITH CORRECT 'IS' INSTEAD OF 'IZ':\n   ", h)













