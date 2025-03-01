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

        # Existing buttons for cloze functionality
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

        # New Export button to navigate to the export screen
        export_btn = tk.Button(
            button_frame, text="Export", command=self.show_export_screen
        )
        export_btn.pack(side=tk.LEFT, padx=5)

        # Copy to Clipboard button remains on the main screen
        copy_btn = tk.Button(
            button_frame, text="Copy to Clipboard", command=self.copy_to_clipboard
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

        # Wrap the selected text with cloze deletion tags
        new_text = f"{{{{c{self.current_tag_num}::{selected_text}}}}}"
        self.input_text.delete(start, end)
        self.input_text.insert(start, new_text)
        return "break"

    def wrap_selected_text_and_increment(self, event):
        # Increment tag number before wrapping text for a new flashcard
        if self.current_tag_num == 1:
            self.current_tag_num = 2
        else:
            self.current_tag_num += 1

        self.wrap_selected_text(event)
        return "break"

    def update_preview(self):
        # Update the flashcard preview based on the input text
        text = self.input_text.get("1.0", tk.END).strip()
        flashcards = generate_flashcards(text)
        preview_str = ""
        if not flashcards:
            preview_str = "Start adding cloze deletions to generate flashcards."
        else:
            for card in flashcards:
                preview_str += f"Flashcard {card['tag']}:\n"
                preview_str += f"\nFront: {card['front']}\n"
                preview_str += f"\nBack: {card['back']}\n\n"
                preview_str += "-" * 40 + "\n\n"
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, preview_str)
        self.output_text.configure(state="disabled")

    def copy_to_clipboard(self):
        # Copy the generated flashcards to the clipboard
        self.output_text.configure(state="normal")
        content = self.output_text.get("1.0", tk.END)
        self.output_text.configure(state="disabled")
        self.clipboard_clear()
        self.clipboard_append(content)
        messagebox.showinfo("Copied", "Flashcards copied to clipboard!")

    def show_export_screen(self):
        # Create a new window for export functionality
        export_window = tk.Toplevel(self)
        export_window.title("Export")
        export_window.geometry("600x400")

        # Example export-related UI elements
        export_label = tk.Label(
            export_window, text="Export Options", font=("Arial", 16)
        )
        export_label.pack(pady=20)

        # (Place additional export functionality widgets here, e.g., format selection, file save options, etc.)


if __name__ == "__main__":
    app = FlashcardGUI()
    app.mainloop()
