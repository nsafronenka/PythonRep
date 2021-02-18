class Paragraph:
    # Creation of a constructor of the class Paragraph
    def __init__(self, paragraph):
        self.source = paragraph
        # Lower case for the letters in paragraph
        paragraph = paragraph.lower()
        # Removing spaces at the beginning and at the end of the sentences
        paragraph = paragraph.strip()

        # Splitting paragraph into a sentences using dot as a separator
        sentences = paragraph.split(".")
        if '' in sentences:
            # Removing blank sentences if any
            sentences.remove('')
        # Adding new variable for resulting paragraph
        norm_paragraph = ""
        for sentence in sentences:
            # Removing spaces to the left of the sentence
            sentence = sentence.lstrip(" ")
            # Changing first character of the sentence to upper case
            sentence = sentence.capitalize()
            if sentence[-1:] not in {"!", "?"}:
                # Adding dot to the end of the sentence
                sentence += "."
            # Adding sentences to the norm_paragraph
            norm_paragraph += sentence + " "
        self.normalized = norm_paragraph.rstrip(" ")