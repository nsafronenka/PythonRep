class Paragraph:
    def __init__(self, paragraph):
        self.source = paragraph
        paragraph = paragraph.lower()           # Lower case for the letters in paragraph
        paragraph = paragraph.strip()           # Removing spaces at the beginning and at the end of the sentences

        sentences = paragraph.split(".")        # Splitting paragraph into a sentences using dot as a separator
        if '' in sentences:
            sentences.remove('')                # Removing blank sentences if any
        norm_paragraph = ""                     # Adding new variable for resulting paragraph
        for sentence in sentences:
            sentence = sentence.lstrip(" ")     # Removing spaces to the left of the sentence
            sentence = sentence.capitalize()    # Changing first character of the sentence to upper case
            if sentence[-1:] not in {"!", "?"}:
                sentence += "."                 # Adding dot to the end of the sentence
            norm_paragraph += sentence + " "    # Adding sentences to the norm_paragraph
        self.normalized = norm_paragraph.rstrip(" ")