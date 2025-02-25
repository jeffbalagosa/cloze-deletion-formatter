import tkinter as tk
from tkinter import scrolledtext
from cloze_parser import generate_flashcards


class FlashcardGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cloze Deletion Flashcard Generator")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Input Label and Text Area
        input_label = tk.Label(self, text="Input Notes:")
        input_label.pack(anchor="nw", padx=10, pady=(10, 0))

        self.input_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=10)
        self.input_text.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)
        self.input_text.bind("<<Modified>>", self.on_input_change)

        # Output Label and Text Area
        output_label = tk.Label(self, text="Flashcard Preview:")
        output_label.pack(anchor="nw", padx=10, pady=(10, 0))

        self.output_text = scrolledtext.ScrolledText(
            self, wrap=tk.WORD, height=10, state="disabled"
        )
        self.output_text.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

    def on_input_change(self, event):
        # When the input text is modified, update the preview
        self.input_text.edit_modified(False)
        self.update_preview()

    def update_preview(self):
        # Get the input text
        text = self.input_text.get("1.0", tk.END).strip()
        flashcards = generate_flashcards(text)

        # Build a preview string from the flashcards
        preview_str = ""
        if not flashcards:
            preview_str = "No cloze deletions found."
        else:
            for card in flashcards:
                preview_str += f"Flashcard for tag c{card['tag']}:\n"
                preview_str += f"Question: {card['question']}\n"
                preview_str += f"Answer: {card['answer']}\n"
                preview_str += "-" * 40 + "\n"

        # Update the output text widget
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, preview_str)
        self.output_text.configure(state="disabled")


if __name__ == "__main__":
    app = FlashcardGUI()
    app.mainloop()
