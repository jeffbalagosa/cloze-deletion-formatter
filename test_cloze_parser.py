import unittest
from cloze_parser import generate_flashcards


class TestClozeParser(unittest.TestCase):
    def test_single_cloze(self):
        input_text = "This is a {{c1::test}}."
        cards = generate_flashcards(input_text)
        self.assertEqual(len(cards), 1)
        card = cards[0]
        self.assertEqual(card["tag"], "1")
        self.assertEqual(card["question"], "This is a _____.")
        self.assertEqual(card["answer"], "This is a test.")
        self.assertEqual(card["cloze_texts"], ["test"])

    def test_multiple_occurrences_same_tag(self):
        input_text = "First: {{c1::alpha}}, then: {{c1::beta}}."
        cards = generate_flashcards(input_text)
        self.assertEqual(len(cards), 1)
        card = cards[0]
        self.assertEqual(card["tag"], "1")
        self.assertEqual(card["question"], "First: _____, then: _____.")
        self.assertEqual(card["answer"], "First: alpha, then: beta.")
        self.assertEqual(card["cloze_texts"], ["alpha", "beta"])

    def test_multiple_cloze_different_tags(self):
        input_text = "Learning {{c1::Python}} is fun, and {{c2::Java}} too."
        cards = generate_flashcards(input_text)
        # Expecting two flashcards for two distinct tags.
        self.assertEqual(len(cards), 2)
        # Sort the cards by tag number for consistency
        cards.sort(key=lambda c: int(c["tag"]))

        card1 = cards[0]
        card2 = cards[1]

        self.assertEqual(card1["tag"], "1")
        self.assertEqual(card1["question"], "Learning _____ is fun, and _____ too.")
        self.assertEqual(card1["answer"], "Learning Python is fun, and Java too.")
        self.assertEqual(card1["cloze_texts"], ["Python"])

        self.assertEqual(card2["tag"], "2")
        self.assertEqual(card2["question"], "Learning _____ is fun, and _____ too.")
        self.assertEqual(card2["answer"], "Learning Python is fun, and Java too.")
        self.assertEqual(card2["cloze_texts"], ["Java"])

    def test_no_cloze(self):
        input_text = "No cloze deletion here."
        cards = generate_flashcards(input_text)
        # Expecting an empty list if no cloze tags are found.
        self.assertEqual(cards, [])


if __name__ == "__main__":
    unittest.main()
