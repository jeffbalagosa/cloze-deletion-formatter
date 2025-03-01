import tkinter as tk
from tkinter import scrolledtext, messagebox
from cloze_parser import generate_flashcards
from export import export_flashcards


class FlashcardGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cloze Deletion Flashcard Generator")
        self.geometry("800x600")
        self.current_tag_num = 1  # Track the current tag number
        self.create_widgets()

    def clear_all(self):
        # Clear the input text area
        self.input_text.delete("1.0", tk.END)

        # Reset the tag counter to 1
        self.current_tag_num = 1

        # Clear the output preview
        self.output_text.configure(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.configure(state="disabled")

        # Show confirmation message
        messagebox.showinfo(
            "Clear", "All inputs have been cleared and tag counter reset to 1."
        )

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

        # Adding Clear button
        clear_btn = tk.Button(button_frame, text="Clear All", command=self.clear_all)
        clear_btn.pack(side=tk.LEFT, padx=5)

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
        export_window.geometry("600x500")

        # Title Label
        title_label = tk.Label(export_window, text="Export Options", font=("Arial", 16))
        title_label.pack(pady=10)

        # Frame for Field Separator Options
        field_frame = tk.LabelFrame(
            export_window, text="Field Separator (Front/Back)", padx=10, pady=10
        )
        field_frame.pack(fill="x", padx=20, pady=10)

        self.field_sep_option = tk.StringVar(value="tab")
        tk.Radiobutton(
            field_frame,
            text="Tab (default)",
            variable=self.field_sep_option,
            value="tab",
            command=self.update_field_custom_visibility,
        ).pack(anchor="w")
        tk.Radiobutton(
            field_frame,
            text="Comma",
            variable=self.field_sep_option,
            value="comma",
            command=self.update_field_custom_visibility,
        ).pack(anchor="w")
        tk.Radiobutton(
            field_frame,
            text="Custom",
            variable=self.field_sep_option,
            value="custom",
            command=self.update_field_custom_visibility,
        ).pack(anchor="w")

        self.custom_field_entry = tk.Entry(field_frame)
        # Initially hide custom entry
        self.custom_field_entry.pack_forget()

        # Frame for Record Separator Options
        record_frame = tk.LabelFrame(
            export_window,
            text="Record Separator (Between Flashcards)",
            padx=10,
            pady=10,
        )
        record_frame.pack(fill="x", padx=20, pady=10)

        self.record_sep_option = tk.StringVar(value="newline")
        tk.Radiobutton(
            record_frame,
            text="New Line (default)",
            variable=self.record_sep_option,
            value="newline",
            command=self.update_record_custom_visibility,
        ).pack(anchor="w")
        tk.Radiobutton(
            record_frame,
            text="Semicolon",
            variable=self.record_sep_option,
            value="semicolon",
            command=self.update_record_custom_visibility,
        ).pack(anchor="w")
        tk.Radiobutton(
            record_frame,
            text="Custom",
            variable=self.record_sep_option,
            value="custom",
            command=self.update_record_custom_visibility,
        ).pack(anchor="w")

        self.custom_record_entry = tk.Entry(record_frame)
        self.custom_record_entry.pack_forget()

        # Export Action Button
        export_action_btn = tk.Button(
            export_window,
            text="Export Flashcards",
            command=lambda: self.perform_export(export_window),
        )
        export_action_btn.pack(pady=10)

        # Exported Output Area
        output_label = tk.Label(export_window, text="Exported Data:")
        output_label.pack(pady=(10, 0))
        self.export_output_text = scrolledtext.ScrolledText(
            export_window, wrap=tk.WORD, height=10, state="disabled"
        )
        self.export_output_text.pack(fill="both", padx=20, pady=5, expand=True)

        # Copy Exported Data Button
        copy_export_btn = tk.Button(
            export_window, text="Copy Exported Data", command=self.copy_exported_data
        )
        copy_export_btn.pack(pady=10)

    def update_field_custom_visibility(self):
        # Show custom field separator entry if 'custom' is selected; otherwise hide it.
        if self.field_sep_option.get() == "custom":
            self.custom_field_entry.pack(anchor="w", pady=5)
            self.custom_field_entry.delete(0, tk.END)
            self.custom_field_entry.insert(0, "")
        else:
            self.custom_field_entry.pack_forget()

    def update_record_custom_visibility(self):
        # Show custom record separator entry if 'custom' is selected; otherwise hide it.
        if self.record_sep_option.get() == "custom":
            self.custom_record_entry.pack(anchor="w", pady=5)
            self.custom_record_entry.delete(0, tk.END)
            self.custom_record_entry.insert(0, "")
        else:
            self.custom_record_entry.pack_forget()

    def perform_export(self, export_window):
        # Generate flashcards from the input text
        text = self.input_text.get("1.0", tk.END).strip()
        flashcards = generate_flashcards(text)
        if not flashcards:
            messagebox.showwarning("Export Warning", "No flashcards to export!")
            return

        # Get the field separator setting
        field_opt = self.field_sep_option.get()
        custom_field = self.custom_field_entry.get() if field_opt == "custom" else None

        # Get the record separator setting
        record_opt = self.record_sep_option.get()
        custom_record = (
            self.custom_record_entry.get() if record_opt == "custom" else None
        )

        # Call the export function to get the exported text
        exported_text = export_flashcards(
            flashcards,
            field_option=field_opt,
            record_option=record_opt,
            custom_field=custom_field,
            custom_record=custom_record,
        )

        # Display the exported text in the export output area
        self.export_output_text.configure(state="normal")
        self.export_output_text.delete("1.0", tk.END)
        self.export_output_text.insert(tk.END, exported_text)
        self.export_output_text.configure(state="disabled")

    def copy_exported_data(self):
        # Copy the exported text from the export output area to the clipboard
        exported_text = self.export_output_text.get("1.0", tk.END)
        if not exported_text.strip():
            messagebox.showwarning("Copy Warning", "No exported data to copy!")
            return
        self.clipboard_clear()
        self.clipboard_append(exported_text)
        messagebox.showinfo("Copied", "Exported data copied to clipboard!")


if __name__ == "__main__":
    app = FlashcardGUI()
    app.mainloop()
