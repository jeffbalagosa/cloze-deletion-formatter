import re


def generate_flashcards(input_text):
    # Regex pattern to capture cloze deletion tags of the form {{c<number>::text}}
    pattern = re.compile(r"\{\{c(\d+)::(.*?)\}\}")

    # Dictionary to hold cloze texts for each tag
    cloze_texts_dict = {}

    # First pass: collect all cloze texts for each tag
    for match in pattern.finditer(input_text):
        tag = match.group(1)
        cloze_text = match.group(2)
        cloze_texts_dict.setdefault(tag, []).append(cloze_text)

    flashcards = []
    # For each unique tag, generate a question view that blanks only that tag
    for tag, texts in cloze_texts_dict.items():

        def make_repl(m, target=tag):
            # If this is the target tag, replace with a placeholder,
            # otherwise, replace with the cloze text (i.e. show the answer)
            return "_____" if m.group(1) == target else m.group(2)

        question_text = pattern.sub(make_repl, input_text)
        flashcards.append(
            {
                "tag": tag,
                "front": question_text,  # Changed from "question" to "front"
                "back": texts,  # Changed from "answer" to "back"
                "cloze_texts": texts,  # Keep this field for backwards compatibility
            }
        )
    return flashcards
