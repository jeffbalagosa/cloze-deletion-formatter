import re


def generate_flashcards(input_text):
    # Regex pattern to capture cloze deletion tags of the form {{c<number>::text}}
    pattern = re.compile(r"\{\{c(\d+)::(.*?)\}\}")

    # Dictionary to hold unique flashcards per cloze tag number
    flashcards = {}

    # Replacement function to build the question view and store cloze texts
    def replacement(match):
        tag = match.group(1)
        cloze_text = match.group(2)
        # Store the cloze text for this tag
        flashcards.setdefault(tag, {"tag": tag, "cloze_texts": []})
        flashcards[tag]["cloze_texts"].append(cloze_text)
        # Replace the cloze deletion with a blank placeholder
        return "_____"

    # Create the question view by substituting cloze tags with placeholders
    question_text = pattern.sub(replacement, input_text)
    # Create the answer view by stripping out the cloze markers but keeping the answer text visible
    answer_text = pattern.sub(lambda m: m.group(2), input_text)

    # Consolidate flashcard objects
    cards = []
    for tag, data in flashcards.items():
        cards.append(
            {
                "tag": tag,
                "question": question_text,
                "answer": answer_text,
                "cloze_texts": data["cloze_texts"],
            }
        )

    return cards


# Example usage:
if __name__ == "__main__":
    sample_text = (
        "This is a sample note with a cloze deletion: {{c1::Python}} is awesome. "
        "Remember, {{c1::programming}} can be fun too!"
    )

    flashcards = generate_flashcards(sample_text)

    for card in flashcards:
        print(f"Flashcard for tag c{card['tag']}:")
        print("Question View:", card["question"])
        print("Answer View:", card["answer"])
        print("Cloze Texts:", card["cloze_texts"])
        print("-" * 40)
