import re


def generate_flashcards(input_text):
    """
    Generates flashcards from the given input text containing cloze deletion tags.
    Args:
        input_text (str): The input text containing cloze deletion tags of the form {{c<number>::text}}.
    Returns:
        list: A list of dictionaries, each representing a flashcard with the following keys:
            - "tag" (str): The cloze deletion tag number.
            - "front" (str): The question text with the cloze deletion replaced by a placeholder.
            - "back" (list): A list of texts corresponding to the cloze deletion tag.
            - "cloze_texts" (list): A list of texts corresponding to the cloze deletion tag (for backwards compatibility).
    """
    pattern = re.compile(r"\{\{c(\d+)::(.*?)\}\}")

    cloze_texts_dict = {}

    for match in pattern.finditer(input_text):
        tag = match.group(1)
        cloze_text = match.group(2)
        cloze_texts_dict.setdefault(tag, []).append(cloze_text)

    flashcards = []
    for tag, texts in cloze_texts_dict.items():

        def make_repl(m, target=tag):
            return "_____" if m.group(1) == target else m.group(2)

        question_text = pattern.sub(make_repl, input_text)
        flashcards.append(
            {
                "tag": tag,
                "front": question_text,
                "back": texts,
                "cloze_texts": texts,
            }
        )
    return flashcards
