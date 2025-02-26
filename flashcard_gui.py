import tkinter as tk
from tkinter import scrolledtext, messagebox
from cloze_parser import generate_flashcards


class FlashcardGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cloze Deletion Flashcard Generator")
        self.geometry("800x600")
        self.current_tag_num = 1  # Track the current tag number
        self.create_widgets()

    def create_widgets(self):
        # Input Label and Text Area
        input_label = tk.Label(self, text="Input Notes:")
        input_label.pack(anchor="nw", padx=10, pady=(10, 0))

        self.input_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, height=10)
        self.input_text.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)
        self.input_text.bind("<<Modified>>", self.on_input_change)
        self.input_text.bind("<Control-Shift-C>", self.wrap_selected_text)
        self.input_text.bind(
            "<Control-Alt-Shift-C>", self.wrap_selected_text_and_increment
        )

        # Output Label and Text Area
        output_label = tk.Label(self, text="Flashcard Preview:")
        output_label.pack(anchor="nw", padx=10, pady=(10, 0))

        self.output_text = scrolledtext.ScrolledText(
            self, wrap=tk.WORD, height=10, state="disabled"
        )
        self.output_text.pack(fill=tk.BOTH, padx=10, pady=5, expand=True)

        # Button Frame
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, padx=10, pady=10)

        # Add buttons as alternatives to hotkeys
        cloze_c1_btn = tk.Button(
            button_frame,
            text="Add Cloze (Same Card)",
            command=lambda: self.wrap_selected_text(None),
        )
        cloze_c1_btn.pack(side=tk.LEFT, padx=5)

        cloze_increment_btn = tk.Button(
            button_frame,
            text="Add Cloze (New Card)",
            command=lambda: self.wrap_selected_text_and_increment(None),
        )
        cloze_increment_btn.pack(side=tk.LEFT, padx=5)

        # Add Copy to Clipboard button
        copy_btn = tk.Button(
            button_frame,
            text="Copy to Clipboard",
            command=self.copy_to_clipboard
        )
        copy_btn.pack(side=tk.RIGHT, padx=5)

    def on_input_change(self, event):
        # When the input text is modified, update the preview
        self.input_text.edit_modified(False)
        self.update_preview()

    def wrap_selected_text(self, event):
        try:
            # Get selected text indices
            start = self.input_text.index(tk.SEL_FIRST)
            end = self.input_text.index(tk.SEL_LAST)
            selected_text = self.input_text.get(start, end)
        except tk.TclError:
            return "break"

        # Create the new wrapped text
        new_text = f"{{{{c{self.current_tag_num}::{selected_text}}}}}"

        # Replace the selection with the new text
        self.input_text.delete(start, end)
        self.input_text.insert(start, new_text)
        return "break"  # Prevent further handling of this event

    def wrap_selected_text_and_increment(self, event):
        # For Control-Alt-Shift-C, increment first to start at c2
        if self.current_tag_num == 1:
            self.current_tag_num = 2  # Start at c2
        else:
            self.current_tag_num += 1  # Continue incrementing

        # Then call the regular wrap method
        self.wrap_selected_text(event)
        return "break"

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
                preview_str += f"Flashcard {card['tag']}:\n"
                preview_str += f"\nFront: {card['question']}\n"
                preview_str += f"\nBack: {card['answer']}\n\n"
                preview_str += "-" * 40 + "\n\n"

        # Update the output text widget
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, preview_str)
        self.output_text.configure(state="disabled")

    def copy_to_clipboard(self):
        # Get the content from the output text widget
        self.output_text.configure(state="normal")
        content = self.output_text.get("1.0", tk.END)
        self.output_text.configure(state="disabled")

        # Clear clipboard and append the new content
        self.clipboard_clear()
        self.clipboard_append(content)

        # Provide feedback to the user
        messagebox.showinfo("Copied", "Flashcards copied to clipboard!")


if __name__ == "__main__":
    app = FlashcardGUI()
    app.mainloop()
